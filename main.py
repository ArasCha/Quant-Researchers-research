from request import request_profiles, request_profile_sections, request_profile_connex_profiles, notify_error
from utils import extract_profile_id, extract_profiles_info, filter_profiles, format_data
from db import insert_profile, get_list_of_users_id, get_index, update_index
import time
import traceback
import random


def add_profile_to_db(profile_id: str, profile_url: str):
    
    profile_sections = request_profile_sections(profile_id)
    ready_data = format_data(profile_id, profile_url, profile_sections)

    insert_profile(ready_data)



# search terms to add: quant, trader, trading, algorithmic trader, quant dev, quantitative developer, quantitative risk, risk quant, analyste quantitatif, quant analyst, quant trader, quant researcher, quant trader 
search_terms = ["quantitative%20research", "quantitative%20researcher", "quantitative%20trading", "quantitative%20trader", "quantitative%20analyst"]
circles = ["S", "O"]
# city_ids = [104406358,102436504,103291313,102277331,103112676,102454443,106383538,90009496,90000070]

# shanghai, pékin, amsterdam, shenzhen, tokyo, Mumbai, Boston, Sydney, Toronto, Zug (suisse), Dubai, Casablanca, Abu Dhabi, Montreal, Francfort, Dublin, Rotterdam, Munich, Lausanne, Brusselles
city_ids = [108025228,90010386,104738515,106204383,101728226,103606803,100025096,104769905,102380872,106164952,106750182,90010383,103873152,103925994,102772228]

if __name__ == "__main__":

    for search_term in search_terms:
        for circle in circles:
            for city_id in city_ids:

                print(search_term, circle, city_id)

                for page_number in range(100): # only 100 pages maximum
                    print(page_number)

                    profiles = request_profiles(page_number, search_term, city_id, circle)
                    profiles = [profile for profile in profiles if "navigationUrl" in profile] # dicts that don't have navigationUrl attribute aren't profiles

                    for profile in filter_profiles(profiles):
                        try:
                            raw_profile_url: str = profile["navigationUrl"]
                            
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

    #         for profile in filter_profiles(connex_profiles):
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

