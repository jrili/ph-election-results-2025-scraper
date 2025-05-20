import requests
from urllib.parse import urljoin
from time import sleep
from json.decoder import JSONDecodeError
import os
import json

from src import logging_utils
from src import config

available_top_levels = ['local', 'overseas']

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

    except JSONDecodeError as e:
        logging_utils.logger.error(f"Error getting JSON from '{url}': {e}")
        sleep(config.REQUEST_SLEEP_S)
        return None

def get_region_er_json(top_level, src_category_code, code=0):
    """ Get the JSON response for the top level and categories 2 to 5 regions

    Keyword Arugments:
    top_level -- string; `local` or `overseas`
    code -- string; `code`.json to fetch

    Return:
    JSON response object
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

logging_utils.init_logger()
logging_utils.logger.info("PH Election Results 2025 Scraper: Started.")

if __name__ == "__main__":
    # TOP-LEVEL: local, overseas
    for top_level_num, top_level in enumerate(available_top_levels):
        logging_utils.logger.debug(f"({top_level_num+1}/{len(available_top_levels)}) Getting data for top level: '{top_level}'")

        cat2_jsons = get_region_er_json(top_level, src_category_code=0)
        if cat2_jsons == None:
            logging_utils.logger.warning(f"Unable to get Category 2 JSON data from top_level: {top_level}. Skipping.")
            continue

        # Write the top-level json file containing category code 2 regions
        write_json(cat2_jsons,
                get_output_path([],
                                f"{top_level}.json"))

        # CATEGORY 2: Local Regions, Overseas Voter Types
        total_num_regions = len(cat2_jsons['regions'])
        for cat2_json_num, cat2_json in enumerate(cat2_jsons['regions']):
            logging_utils.logger.debug(f"({cat2_json_num+1}/{total_num_regions}) Getting data from local region/overseas voter type: '{cat2_json['code']}'({cat2_json['name']})")

            cat3_jsons = get_region_er_json(top_level, src_category_code=2, code=cat2_json['code'])

            if cat3_jsons == None:
                logging_utils.logger.warning(f"Unable to get Category 3 JSON data from top_level: {top_level}, category 2 code: {cat2_json['code']}({cat2_json['name']}). Skipping.")
                continue

            # Write the category 2 json file containing category code 3 regions
            write_json(cat3_jsons,
                    get_output_path([
                                        top_level
                                    ],
                                    f"{cat2_json['code']}.json"))

            # CATEGORY 3: Local Provinces, Global Regions
            total_num_provinces = len(cat3_jsons['regions'])
            for cat3_json_num, cat3_json in enumerate(cat3_jsons['regions']):
                logging_utils.logger.info(f"({cat3_json_num+1}/{total_num_provinces}) Getting data from province/global region '{cat3_json['code']}'({cat3_json['name']})")

                cat4_jsons = get_region_er_json(top_level, src_category_code=3, code=cat3_json['code'])

                if cat4_jsons == None:
                    logging_utils.logger.warning(f"Unable to get Category 4 JSON data from top_level: {top_level}, category 2 code: {cat2_json['code']} ({cat2_json['name']}), category 3 code: {cat3_json['code']} ({cat3_json['name']}). Skipping.")
                    continue

                # Write the category 3 json file containing category code 4 regions
                write_json(cat4_jsons,
                        get_output_path( [
                                            top_level,
                                            f"{cat2_json['code']}"
                                        ],
                                        f"{cat3_json['code']}.json"))

                # CATEGORY 4: Local Municipalities, Overseas Countries
                total_num_municipalities = len(cat4_jsons['regions'])
                for cat4_json_num, cat4_json in enumerate(cat4_jsons['regions']):
                    logging_utils.logger.debug(f"({cat4_json_num+1}/{total_num_municipalities}) Getting data from municipality/country: '{cat4_json['code']}'({cat4_json['name']})")

                    cat5_jsons = get_region_er_json(top_level, src_category_code=4, code=cat4_json['code'])

                    if cat5_jsons == None:
                        logging_utils.logger.warning(f"Unable to get Category 5 JSON data from top_level: {top_level}, category 2 code: {cat2_json['code']} ({cat2_json['name']}), category 3 code: {cat3_json['code']} ({cat3_json['name']}), category 4 code: {cat4_json['code']} ({cat4_json['name']}). Skipping.")
                        continue

                    # Write the category 4 json file containing category code 5 regions
                    write_json(cat5_jsons,
                            get_output_path( [
                                                top_level,
                                                f"{cat2_json['code']}",
                                                f"{cat3_json['code']}"
                                            ],
                                            f"{cat4_json['code']}.json"))

                    # CATEGORY 5: Local Baranggays, Overseas Jurisdictions
                    total_num_brgys = len(cat5_jsons['regions'])
                    for cat5_json_num, cat5_json in enumerate(cat5_jsons['regions']):
                        logging_utils.logger.debug(f"({cat5_json_num+1}/{total_num_brgys}) Getting data from baranggay/jurisdiction: '{cat5_json['code']}'({cat5_json['name']})")

                        precinct_jsons = get_region_er_json(top_level, src_category_code=5, code=cat5_json['code'])

                        if precinct_jsons == None:
                            logging_utils.logger.warning(f"Unable to get precinct JSON data from top_level: {top_level}, category 2 code: {cat2_json['code']} ({cat2_json['name']}), category 3 code: {cat3_json['code']} ({cat3_json['name']}), category 4 code: {cat4_json['code']} ({cat4_json['name']}), category 5 code: {cat5_json['code']} ({cat5_json['name']}). Skipping.")
                            continue

                        # CATEGORY NULL: Precincts
                        for precinct_json in precinct_jsons['regions']:
                            logging_utils.logger.info(f" Getting election results from "\
                                                    f"top level: '{top_level}', "\
                                                    f"cat2 code: '{cat2_json['code']}'({cat2_json['name']}), "\
                                                    f"cat3 code: '{cat3_json['code']}'({cat3_json['name']}), "\
                                                    f"cat4 code: '{cat4_json['code']}'({cat4_json['name']}), "\
                                                    f"cat5 code: '{cat5_json['code']}'({cat5_json['name']}), "\
                                                    f"precinct code: '{precinct_json['code']}'")

                            er_jsons = get_region_er_json(top_level, src_category_code=None, code=precinct_json['code'])

                            if er_jsons == None:
                                logging_utils.logger.warning(f"Unable to get election results JSON data from top_level: {top_level}, category 2 code: {cat2_json['code']} ({cat2_json['name']}), category 3 code: {cat3_json['code']} ({cat3_json['name']}), category 4 code: {cat4_json['code']} ({cat4_json['name']}), category 5 code: {cat5_json['code']} ({cat5_json['name']}), precinct code: {precinct_json['code']}. Skipping.")
                                continue

                            # Write the category 5 json file containing precinct data
                            write_json(er_jsons,
                                    get_output_path( [
                                                        top_level,
                                                        f"{cat2_json['code']}",
                                                        f"{cat3_json['code']}",
                                                        f"{cat4_json['code']}",
                                                        f"{cat5_json['code']}"
                                                    ],
                                                    f"{precinct_json['code']}.json"))

    logging_utils.logger.info("PH Election Results 2025 Scraper: Ended.")
