import requests
from urllib.parse import urljoin
from time import sleep
from json.decoder import JSONDecodeError

from src import logging_utils
from src import config

available_top_levels = ['local', 'overseas']

def get_json(url):
    logging_utils.logger.debug(f"In get_json(): Getting from url: '{url}'")
    try: 
        response = requests.get(url)

        if response.status_code != 200:
            logging_utils.logger.warning(f"Unable to get JSON from '{url}'. Skipping")
            sleep(config.REQUEST_SLEEP_S)
            return None

        response_json = response.json()
        logging_utils.logger.debug(f"response_json: {response_json}")

        logging_utils.logger.debug(f"In get_json(): Ended")
        sleep(config.REQUEST_SLEEP_S)
        return response_json

    except JSONDecodeError as e:
        logging_utils.logger.error(f"Error getting JSON from '{url}': {e}")
        sleep(config.REQUEST_SLEEP_S)
        return None

def get_region_json(top_level, src_category_code, code=0):
    """ Get the JSON response for the top level and categories 2 to 5 regions

    Keyword Arugments:
    top_level -- string; `local` or `overseas`
    code -- string; `code`.json to fetch

    Return:
    JSON response object
    """
    logging_utils.logger.debug(f"In get_region_json(): Started w/ top_level={top_level}, category_code={src_category_code}, code={code}")

    url = ""
    # For top-level, category codes 2 to 4:
    if src_category_code < 5:
        url = urljoin(config.BASE_URL, top_level)
        url = urljoin(url + '/', f"{code}.json")
    # For baranggay/jurisdiction level
    elif src_category_code == 5:
        url = urljoin(config.BASE_URL, "precinct")
        url = urljoin(url + '/', code[0:2])
        url = urljoin(url + '/', f"{code}.json")

    response_json = get_json(url)
    logging_utils.logger.debug(f"In get_region_json(): Ended")

    return response_json


logging_utils.init_logger()
logging_utils.logger.info("PH Election Results 2025 Scraper: Started.")

# Top level:
for top_level_num, top_level in enumerate(available_top_levels):
    logging_utils.logger.info(f"({top_level_num+1}/{len(available_top_levels)}) Getting category 2 data from top level: '{top_level}'")

    cat2_jsons = get_region_json(top_level, src_category_code=0)
    if cat2_jsons == None:
        logging_utils.logger.warning(f"Unable to get Category 2 JSON data from top_level: {top_level}. Skipping.")
        continue

    # Local Regions, Overseas Voter Types
    for cat2_json_num, cat2_json in enumerate(cat2_jsons['regions']):
        logging_utils.logger.info(f"\t({cat2_json_num+1}/{len(cat2_jsons['regions'])}) Getting category 3 data from category 2 code: '{cat2_json['code']}'({cat2_json['name']})")

        cat3_jsons = get_region_json(top_level, src_category_code=2, code=cat2_json['code'])

        if cat3_jsons == None:
            logging_utils.logger.warning(f"Unable to get Category 3 JSON data from top_level: {top_level}, category 2 code: {cat2_json['code']}({cat2_json['name']}). Skipping.")
            continue

        # Local Provinces, Global Regions
        for cat3_json_num, cat3_json in enumerate(cat3_jsons['regions']):
            logging_utils.logger.info(f"\t\t({cat3_json_num+1}/{len(cat3_jsons['regions'])}) Getting category 4 data from category 3 code: '{cat3_json['code']}'({cat3_json['name']})")

            cat4_jsons = get_region_json(top_level, src_category_code=3, code=cat3_json['code'])

            if cat4_jsons == None:
                logging_utils.logger.warning(f"Unable to get Category 4 JSON data from top_level: {top_level}, category 2 code: {cat2_json['code']} ({cat2_json['name']}), category 3 code: {cat3_json['code']} ({cat3_json['name']}). Skipping.")
                continue

            # Local Municipalities, Overseas Countries
            for cat4_json_num, cat4_json in enumerate(cat4_jsons['regions']):
                logging_utils.logger.info(f"\t\t\t({cat4_json_num+1}/{len(cat4_jsons['regions'])}) Getting category 5 data from category 4 code: '{cat4_json['code']}'({cat4_json['name']})")

                cat5_jsons = get_region_json(top_level, src_category_code=4, code=cat4_json['code'])

                if cat5_jsons == None:
                    logging_utils.logger.warning(f"Unable to get Category 5 JSON data from top_level: {top_level}, category 2 code: {cat2_json['code']} ({cat2_json['name']}), category 3 code: {cat3_json['code']} ({cat3_json['name']}), category 4 code: {cat4_json['code']} ({cat4_json['name']}). Skipping.")
                    continue

                # Local Baranggays, Overseas Jurisdictions
                total_num_regions = len(cat5_jsons['regions'])
                for cat5_json_num, cat5_json in enumerate(cat5_jsons['regions']):
                    logging_utils.logger.info(f"\t\t\t\t({cat5_json_num+1}/{total_num_regions}) Getting precinct data from category 5 code: '{cat5_json['code']}'({cat5_json['name']})")

                    precinct_jsons = get_region_json(top_level, src_category_code=5, code=cat5_json['code'])

                    if precinct_jsons == None:
                        logging_utils.logger.warning(f"Unable to get precinct JSON data from top_level: {top_level}, category 2 code: {cat2_json['code']} ({cat2_json['name']}), category 3 code: {cat3_json['code']} ({cat3_json['name']}), category 4 code: {cat4_json['code']} ({cat4_json['name']}), category 5 code: {cat5_json['code']} ({cat5_json['name']}). Skipping.")
                        continue


logging_utils.logger.info("PH Election Results 2025 Scraper: Ended.")
