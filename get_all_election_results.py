from time import time
from math import trunc
import json
import os

from src import logging_utils
from src.extract_utils import get_region_er_json, write_json, get_output_path

available_top_levels = ['local', 'overseas']

if __name__ == "__main__":

    start_time = time()
    logging_utils.init_logger()
    logging_utils.logger.info("PH Election Results 2025 Scraper: Started.")

    # TOP-LEVEL: local, overseas
    for top_level_num, top_level in enumerate(available_top_levels):
        logging_utils.logger.debug(f"({top_level_num+1}/{len(available_top_levels)}) Getting data for top level: '{top_level}'")

        path_to_output_file = get_output_path([], f"{top_level}.json")
        cat2_jsons = {}

        # Skip getting and saving if existing (presumed previously downloaded)
        if not os.path.exists(path_to_output_file):
            cat2_jsons = get_region_er_json(top_level, src_category_code=0)
            if cat2_jsons == None:
                logging_utils.logger.warning(f"Unable to get Category 2 JSON data from top_level: {top_level}. Skipping.")
                continue

            # Write the top-level json file containing category code 2 regions
            write_json(cat2_jsons, path_to_output_file)

        else:
            with open(path_to_output_file, 'r') as f:
                cat2_jsons = json.load(f)

        # CATEGORY 2: Local Regions, Overseas Voter Types
        total_num_regions = len(cat2_jsons['regions'])
        for cat2_json_num, cat2_json in enumerate(cat2_jsons['regions']):
            logging_utils.logger.debug(f"({cat2_json_num+1}/{total_num_regions}) Getting data from local region/overseas voter type: '{cat2_json['code']}'({cat2_json['name']})")

            path_to_output_file = get_output_path([top_level], f"{cat2_json['code']}.json")
            cat3_jsons = {}

            # Skip getting and saving if existing (presumed previously downloaded)
            if not os.path.exists(path_to_output_file):
                cat3_jsons = get_region_er_json(top_level, src_category_code=2, code=cat2_json['code'])

                if cat3_jsons == None:
                    logging_utils.logger.warning(f"Unable to get Category 3 JSON data from top_level: {top_level}, category 2 code: {cat2_json['code']}({cat2_json['name']}). Skipping.")
                    continue

                # Write the category 2 json file containing category code 3 regions
                write_json(cat3_jsons, path_to_output_file)

            else:
                with open(path_to_output_file, 'r') as f:
                    cat3_jsons = json.load(f)

            # CATEGORY 3: Local Provinces, Global Regions
            total_num_provinces = len(cat3_jsons['regions'])
            for cat3_json_num, cat3_json in enumerate(cat3_jsons['regions']):
                logging_utils.logger.info(f"({cat3_json_num+1}/{total_num_provinces}) Getting data from province/global region '{cat3_json['code']}'({cat3_json['name']})")

                path_to_output_file = get_output_path( [ top_level,
                                              f"{cat2_json['code']}"
                                            ],
                                            f"{cat3_json['code']}.json")
                cat4_jsons = {}

                # Skip getting and saving if existing (presumed previously downloaded)
                if not os.path.exists(path_to_output_file):
                    cat4_jsons = get_region_er_json(top_level, src_category_code=3, code=cat3_json['code'])

                    if cat4_jsons == None:
                        logging_utils.logger.warning(f"Unable to get Category 4 JSON data from top_level: {top_level}, category 2 code: {cat2_json['code']} ({cat2_json['name']}), category 3 code: {cat3_json['code']} ({cat3_json['name']}). Skipping.")
                        continue

                    # Write the category 3 json file containing category code 4 regions
                    write_json(cat4_jsons, path_to_output_file)

                else:
                    with open(path_to_output_file, 'r') as f:
                        cat4_jsons = json.load(f)

                # CATEGORY 4: Local Municipalities, Overseas Countries
                total_num_municipalities = len(cat4_jsons['regions'])
                for cat4_json_num, cat4_json in enumerate(cat4_jsons['regions']):
                    logging_utils.logger.debug(f"({cat4_json_num+1}/{total_num_municipalities}) Getting data from municipality/country: '{cat4_json['code']}'({cat4_json['name']})")

                    path_to_output_file = get_output_path( [top_level,
                                                  f"{cat2_json['code']}",
                                                  f"{cat3_json['code']}"
                                                ],
                                                f"{cat4_json['code']}.json")
                    cat5_jsons = {}

                    # Skip getting and saving if existing (presumed previously downloaded)
                    if not os.path.exists(path_to_output_file):
                        cat5_jsons = get_region_er_json(top_level, src_category_code=4, code=cat4_json['code'])

                        if cat5_jsons == None:
                            logging_utils.logger.warning(f"Unable to get Category 5 JSON data from top_level: {top_level}, category 2 code: {cat2_json['code']} ({cat2_json['name']}), category 3 code: {cat3_json['code']} ({cat3_json['name']}), category 4 code: {cat4_json['code']} ({cat4_json['name']}). Skipping.")
                            continue

                        # Write the category 4 json file containing category code 5 regions
                        write_json(cat5_jsons, path_to_output_file)

                    else:
                        with open(path_to_output_file, 'r') as f:
                            cat5_jsons = json.load(f)

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
                                                    f"'{top_level}'| "\
                                                    f"'{cat2_json['code']}'({cat2_json['name']})| "\
                                                    f"'{cat3_json['code']}'({cat3_json['name']})| "\
                                                    f"'{cat4_json['code']}'({cat4_json['name']})| "\
                                                    f"'{cat5_json['code']}'({cat5_json['name']})| "\
                                                    f"'{precinct_json['code']}'")

                            path_to_output_file = get_output_path( [top_level,
                                                        f"{cat2_json['code']}",
                                                        f"{cat3_json['code']}",
                                                        f"{cat4_json['code']}",
                                                        f"{cat5_json['code']}"
                                                    ],
                                                    f"{precinct_json['code']}.json")
                            er_jsons = {}

                            # Skip getting and saving if existing (presumed previously downloaded)
                            if not os.path.exists(path_to_output_file):
                                er_jsons = get_region_er_json(top_level, src_category_code=None, code=precinct_json['code'])

                                if er_jsons == None:
                                    logging_utils.logger.warning(f"Unable to get election results JSON data from top_level: {top_level}, category 2 code: {cat2_json['code']} ({cat2_json['name']}), category 3 code: {cat3_json['code']} ({cat3_json['name']}), category 4 code: {cat4_json['code']} ({cat4_json['name']}), category 5 code: {cat5_json['code']} ({cat5_json['name']}), precinct code: {precinct_json['code']}. Skipping.")
                                    continue

                                # Write the precinct-level election results
                                write_json(er_jsons, path_to_output_file)
                            else:
                                logging_utils.logger.info(f"\tFile already downloaded in '{path_to_output_file}'. Skipping.")

    elapsed_time = time() - start_time
    logging_utils.logger.info(f"PH Election Results 2025 Scraper: Ended in {trunc(elapsed_time//(60*60))}h {trunc((elapsed_time//60) % 60)}m {trunc(elapsed_time % 60)}s")
