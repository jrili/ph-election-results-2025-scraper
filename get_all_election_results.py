from time import time
from math import trunc
import json
import os
import logging

from src import logging_utils
from src.extract_utils import extract_region_er_json, extract_top_level_json

available_top_levels = ['local', 'overseas']

if __name__ == "__main__":

    start_time = time()
    logging_utils.init_logger(level = logging.DEBUG, console_level = logging.WARNING)
    logging_utils.logger.info("PH Election Results 2025 Scraper: Started.")

    # TOP-LEVEL: local, overseas
    for top_level_num, top_level in enumerate(available_top_levels):
        logging_utils.logger.debug(f"({top_level_num+1}/{len(available_top_levels)}) Getting data for top level: '{top_level}'")

        cat2_jsons = extract_top_level_json(top_level)
        if cat2_jsons == None:
            continue

        # CATEGORY 2: Local Regions, Overseas Voter Types
        total_num_regions = len(cat2_jsons['regions'])
        for cat2_json_num, cat2_json in enumerate(cat2_jsons['regions']):
            logging_utils.logger.debug(f"({cat2_json_num+1}/{total_num_regions}) Getting data from local region/overseas voter type: '{cat2_json['code']}'({cat2_json['name']})")

            cat3_jsons = extract_region_er_json(parents=[top_level],
                                            code=cat2_json['code'],
                                            top_level = top_level,
                                            src_category_code=2)
            if cat3_jsons == None:
                continue

            # CATEGORY 3: Local Provinces, Global Regions
            total_num_provinces = len(cat3_jsons['regions'])
            for cat3_json_num, cat3_json in enumerate(cat3_jsons['regions']):
                logging_utils.logger.info(f"({cat3_json_num+1}/{total_num_provinces}) Getting data from province/global region '{cat3_json['code']}'({cat3_json['name']})")

                cat4_jsons = extract_region_er_json(parents=[top_level,
                                                    f"{cat2_json['code']}",
                                                ],
                                                code=cat3_json['code'],
                                                top_level = top_level,
                                                src_category_code=3)
                if cat4_jsons == None:
                    continue

                # CATEGORY 4: Local Municipalities, Overseas Countries
                total_num_municipalities = len(cat4_jsons['regions'])
                for cat4_json_num, cat4_json in enumerate(cat4_jsons['regions']):
                    logging_utils.logger.debug(f"({cat4_json_num+1}/{total_num_municipalities}) Getting data from municipality/country: '{cat4_json['code']}'({cat4_json['name']})")

                    cat5_jsons = extract_region_er_json(parents=[top_level,
                                                        f"{cat2_json['code']}",
                                                        f"{cat3_json['code']}",
                                                    ],
                                                    code=cat4_json['code'],
                                                    top_level = top_level,src_category_code=4)
                    if cat5_jsons == None:
                        continue

                    # CATEGORY 5: Local Baranggays, Overseas Jurisdictions
                    total_num_brgys = len(cat5_jsons['regions'])
                    for cat5_json_num, cat5_json in enumerate(cat5_jsons['regions']):
                        logging_utils.logger.debug(f"({cat5_json_num+1}/{total_num_brgys}) Getting data from baranggay/jurisdiction: '{cat5_json['code']}'({cat5_json['name']})")

                        precinct_jsons = extract_region_er_json(parents=[top_level,
                                                        f"{cat2_json['code']}",
                                                        f"{cat3_json['code']}",
                                                        f"{cat4_json['code']}",
                                                    ],
                                                    code=cat5_json['code'],
                                                    top_level = top_level,
                                                    src_category_code=5)
                        if precinct_jsons == None:
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
                            
                            extract_region_er_json(parents=[top_level,
                                                        f"{cat2_json['code']}",
                                                        f"{cat3_json['code']}",
                                                        f"{cat4_json['code']}",
                                                        f"{cat5_json['code']}"
                                                    ],
                                                    code=precinct_json['code'],
                                                    top_level = top_level,
                                                    src_category_code=None,
                                                    return_existing_file_enabled=False)

    elapsed_time = time() - start_time
    logging_utils.logger.info(f"PH Election Results 2025 Scraper: Ended in {trunc(elapsed_time//(60*60))}h {trunc((elapsed_time//60) % 60)}m {trunc(elapsed_time % 60)}s")
