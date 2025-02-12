from request import request_profiles, request_profile_sections, request_profile_connex_profiles, notify_error
from utils import extract_profile_id, extract_profiles_info, filter_connex_profiles, format_data
from db import insert_profile, get_list_of_users_id, get_index, update_index
import time
import traceback
import random


def add_profile_to_db(profile_id: str, profile_url: str):
    
    profile_sections = request_profile_sections(profile_id)
    ready_data = format_data(profile_id, profile_url, profile_sections)

    insert_profile(ready_data)



search_terms = ["quantitative%20research", "quantitative%20researcher", "quantitative%20trading", "quantitative%20trader", "quantitative%20analyst"]
circles = ["S", "O"]
city_ids = [104406358,102436504,103291313,102277331,103112676,102454443,106383538,90009496,90000070]

if __name__ == "__main__":

    for search_term in search_terms:
        for circle in circles:
            for city_id in city_ids:

                for page_number in range(100): # only 100 pages maximum

                    data = request_profiles(page_number, search_term, city_id, circle)

                    profiles = data["included"]
                    print(page_number)

                    for profile in profiles:
                        try:
                            try:
                                raw_profile_url: str = profile["navigationUrl"]
                            except KeyError: # a bunch of irrelevant data will be in data. If it doesn't have the navigationUrl attribute we'll assume it's not a profile
                                continue
                            
                            profile_url = raw_profile_url.split("?")[0] # we keep URI and remove URL parameters
                            profile_id = extract_profile_id(raw_profile_url)

                            if profile_id not in get_list_of_users_id():
                                add_profile_to_db(profile_id, profile_url)
                                print(profile_url)
                                time.sleep(random.gauss(10, 2))

                        except Exception as e:
                            traceback.print_exc()


    # i = get_index()
    # while True:
        
    #     try:

    #         print(i)
    #         root_profile_id = get_list_of_users_id()[i]

    #         raw_connex_profiles = request_profile_connex_profiles(root_profile_id)
    #         connex_profiles = extract_profiles_info(raw_connex_profiles)
    #         filtered_connex_profiles = filter_connex_profiles(connex_profiles)

    #         for profile in filtered_connex_profiles:
    #             if profile["id"] not in get_list_of_users_id():
    #                 add_profile_to_db(profile["id"], profile["url"])
    #                 print(profile["url"])
    #                 time.sleep(10)

    #         i+=1
    #         update_index(i)
    #         time.sleep(10)

    #     except Exception as e:
    #         error_traceback = traceback.print_exc()
    #         notify_error(str(error_traceback))
    #         print(error_traceback)
    #         time.sleep(100)

