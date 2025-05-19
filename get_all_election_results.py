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
    logging_utils.logger.info(f"Getting category 2 data from top level: '{top_level}' ({top_level_num+1}/{len(available_top_levels)})")

    category_2_jsons = get_region_json(top_level, src_category_code=0)
    if category_2_jsons == None:
        logging_utils.logger.warning(f"Unable to get Category 2 JSON data from top_level: {top_level}. Skipping.")
        continue

    # Local Regions, Overseas Voter Types
    for category_2_json_num, category_2_json in enumerate(category_2_jsons['regions']):
        logging_utils.logger.info(f"\tGetting category 3 data from category 2 code: '{category_2_json['code']}'({category_2_json['name']}) ({category_2_json_num+1}/{len(category_2_jsons['regions'])})")

        category_3_jsons = get_region_json(top_level, src_category_code=2, code=category_2_json['code'])

        if category_3_jsons == None:
            logging_utils.logger.warning(f"Unable to get Category 3 JSON data from top_level: {top_level}, category 2 code: {category_2_json['code']}({category_2_json['name']}). Skipping.")
            continue

        # Local Provinces, Global Regions
        for category_3_json_num, category_3_json in enumerate(category_3_jsons['regions']):
            logging_utils.logger.info(f"\t\tGetting category 4 data from category 3 code: '{category_3_json['code']}'({category_3_json['name']}) ({category_3_json_num+1}/{len(category_3_jsons['regions'])})")

            category_4_jsons = get_region_json(top_level, src_category_code=3, code=category_3_json['code'])

            if category_4_jsons == None:
                logging_utils.logger.warning(f"Unable to get Category 4 JSON data from top_level: {top_level}, category 2 code: {category_2_json['code']} ({category_2_json['name']}), category 3 code: {category_3_json['code']} ({category_3_json['name']}). Skipping.")
                continue

            # Local Municipalities, Overseas Countries
            for category_4_json_num, category_4_json in enumerate(category_4_jsons['regions']):
                logging_utils.logger.info(f"\t\t\tGetting category 5 data from category 4 code: '{category_4_json['code']}'({category_4_json['name']}) ({category_4_json_num+1}/{len(category_4_jsons['regions'])})")

                category_5_jsons = get_region_json(top_level, src_category_code=4, code=category_4_json['code'])

                if category_5_jsons == None:
                    logging_utils.logger.warning(f"Unable to get Category 5 JSON data from top_level: {top_level}, category 2 code: {category_2_json['code']} ({category_2_json['name']}), category 3 code: {category_3_json['code']} ({category_3_json['name']}), category 4 code: {category_4_json['code']} ({category_4_json['name']}). Skipping.")
                    continue

                # Local Baranggays, Overseas Jurisdictions
                for category_5_json_num, category_5_json in enumerate(category_5_jsons['regions']):
                    logging_utils.logger.info(f"\t\t\t\tGetting precinct data from category 5 code: '{category_5_json['code']}'({category_5_json['name']}) ({category_5_json_num+1}/{len(category_5_jsons['regions'])})")

                    precinct_jsons = get_region_json(top_level, src_category_code=5, code=category_5_json['code'])

                    if precinct_jsons == None:
                        logging_utils.logger.warning(f"Unable to get precinct JSON data from top_level: {top_level}, category 2 code: {category_2_json['code']} ({category_2_json['name']}), category 3 code: {category_3_json['code']} ({category_3_json['name']}), category 4 code: {category_4_json['code']} ({category_4_json['name']}), category 5 code: {category_5_json['code']} ({category_5_json['name']}). Skipping.")
                        continue


logging_utils.logger.info("PH Election Results 2025 Scraper: Ended.")
