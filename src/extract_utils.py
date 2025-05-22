import requests
from urllib.parse import urljoin
from time import time, sleep
from json.decoder import JSONDecodeError
import os
import json
from math import trunc

from . import logging_utils
from . import config

def get_json(url):
    """Get json data from URL

    Keyword Arguments:

    url -- url to get from

    Return:

    dict containing json data,

    None if http status code is not success or if does not contain json data
    """
    logging_utils.logger.debug(f"In get_json(): Getting from url: '{url}'")
    try: 
        response = requests.get(url)

        if response.status_code != 200:
            logging_utils.logger.warning(f"Unable to get JSON from '{url}'. Skipping")
            sleep(config.REQUEST_SLEEP_S)
            return None

        response_json = response.json()

        logging_utils.logger.debug(f"In get_json(): Ended")
        sleep(config.REQUEST_SLEEP_S)
        return response_json

    except (JSONDecodeError, requests.exceptions.ConnectionError) as e:
        logging_utils.logger.error(f"Error getting JSON from '{url}': {e}")
        sleep(config.REQUEST_SLEEP_S)
        return None

def get_region_er_json(top_level, src_category_code, code="0"):
    """ Get the JSON data for regional data (category codes 0 to 5) or election results data (category code null/None)

    Keyword Arugments:

    top_level -- string; `local` or `overseas`

    src_category_code -- category code from which `code` was taken from

    code -- string; `code`.json to fetch

    Return:

    JSON response object,

    None if call to URL is unsuccessful
    """
    logging_utils.logger.debug(f"In get_region_json(): Started w/ top_level={top_level}, category_code={src_category_code}, code={code}")

    url = ""
    # For precinct-level election results
    if src_category_code is None:
        url = urljoin(config.BASE_ER_URL, code[0:3])
        url = urljoin(url + '/', f"{code}.json")
    # For top-level, category codes 2 to 4:
    elif src_category_code < 5:
        url = urljoin(config.BASE_REGION_URL, top_level)
        url = urljoin(url + '/', f"{code}.json")
    # For baranggay/jurisdiction level
    elif src_category_code == 5:
        url = urljoin(config.BASE_REGION_URL, "precinct")
        url = urljoin(url + '/', code[0:2])
        url = urljoin(url + '/', f"{code}.json")
    

    response_json = get_json(url)
    logging_utils.logger.debug(f"In get_region_json(): Ended")

    return response_json

def write_json(json_data:dict, path_to_file:str):
    """ Write dict object to a json file

    Keyword Arguments:

    json_data -- dict containing json data

    path_to_file -- relative path with respect to working directory upon running main script
        Parent and child directories will be automatically created if not existing

    Return:

    None
    """
    logging_utils.logger.debug(f"In write_json(): path_to_file:'{path_to_file}'")

    file_dir = os.path.dirname(path_to_file)
    if not os.path.exists(file_dir):
        os.makedirs(file_dir, exist_ok=True)

    with open(path_to_file, 'w') as json_file:
        json.dump(json_data, json_file, indent=4)
    
    logging_utils.logger.debug(f"In write_json(): File written to path_to_file:'{path_to_file}'")

def get_output_path(parents:list, filename=None):
    """Return output path organized per region

    Keyword Arguments:

    parents -- list of strings that correspond to region codes of each succeeding parent, e.g.
        ['local', 'R04A000', '3400000', '3403000', '3403008']

    Return:

    String containing path including config.OUTPUT_PATH
    """
    output_path = config.OUTPUT_PATH
    for parent in parents:
        output_path = os.path.join(output_path, f"{parent}")

    if filename is not None:
        output_path = os.path.join(output_path, filename)

    return output_path

def extract_region_er_json(top_level:str, parents:list,
                        src_category_code,
                        code="0",
                        return_existing_file_enabled=True):
    """Extracts region json or election result json data either from previously downloaded file (if existing) or fetched from URL

    Keyword Arguments:
    top_level -- string; `local` or `overseas`

    parents --  list of strings that correspond to region codes of each succeeding parent, e.g. ['local', 'R04A000', '3400000', '3403000', '3403008']

    code -- string; code to be extracted

    src_category_code -- category code from which code was taken from

    return_existing_file_enabled -- enable reading from previously downloaded (already existing) file

    
    Return:

    dict parsed from JSON extracted from URL or previously downloaded file

    None if extracting from URL failed

    None if previously downloaded file exists and return_existing_file_enabled is set to False


    """
    logging_utils.logger.debug(f"In extract_region_er_json(): top_level:{top_level}, parents:{parents}, code:{code}, return:{return_existing_file_enabled}")

    path_to_output_file = get_output_path(parents, f"{code}.json")

    extracted_json = {}

    # Skip getting and saving if existing (presumed previously downloaded)
    if not os.path.exists(path_to_output_file):

        extracted_json = get_region_er_json(top_level,
                                            src_category_code=src_category_code,
                                            code=code)

        if extracted_json == None:
            log_str = f"Unable to get JSON data w/ code '{code}' from "
            for parent in parents:
                log_str = log_str + f" {parent}|"
            log_str = log_str[:-1] + ". Skipping."

            logging_utils.logger.warning(log_str)

        # Write the region/election results json file
        else:
            write_json(extracted_json, path_to_output_file)
    else:
        if return_existing_file_enabled:
            with open(path_to_output_file, 'r') as f:
                extracted_json = json.load(f)
        else:
            logging_utils.logger.info(f"\tFile already downloaded in '{path_to_output_file}'. Skipping.")
            extracted_json = None

    logging_utils.logger.debug(f"In extract_region_er_json(): End")
    return extracted_json

def extract_top_level_json(top_level):
    """ Extracts top-level JSON data specified by `top_level`"""
    extracted_json = extract_region_er_json(top_level=top_level, parents=[], src_category_code="0")
    return extracted_json
