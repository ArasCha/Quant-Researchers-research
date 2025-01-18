from request import request_profiles, request_profile_section, request_profile_connex_profiles, notify_error
from utils import extract_profile_id, extract_data, extract_profiles_url, extract_projects
from db import insert_profile, get_list_of_users_id, get_index, update_index
import time
import traceback
from requests.exceptions import JSONDecodeError




def add_profile_to_db(profile_id, profile_url):
    
    raw_education_data = request_profile_section(profile_id, "education")
    raw_experience_data = request_profile_section(profile_id, "experience")
    raw_certifications_data = request_profile_section(profile_id, "certifications")
    raw_projects_data = request_profile_section(profile_id, "projects")

    print(profile_url)
    insert_profile({
        "profile_id": profile_id,
        "profile_url": profile_url,
        "education": extract_data(raw_education_data,
            {   "school": "titleV2",
                "degree": "subtitle",
                "year": "caption"
            }),
        "experience": extract_data(raw_experience_data,
            {   "job": "titleV2",
                "company": "subtitle",
                "date": "caption",
                "location": "metadata"
            }),
        "certifications": extract_data(raw_certifications_data,
            {   "name": "titleV2",
                "institution": "subtitle",
                "year": "caption"
            }),
        "projects": extract_projects(raw_projects_data)
    })



if __name__ == "__main__":

    # for page_number in range(100): # only 100 pages maximum

    #     data = request_profiles(page_number)

    #     profiles = data["included"]

    #     for profile in profiles:
    #         try:
    #             try:
    #                 raw_profile_url: str = profile["navigationUrl"]
    #             except KeyError: # a bunch of irrelevant data will be in data. If it doesn't have the navigationUrl attribute we'll assume it's not a profile
    #                 continue
                
    #             profile_url = raw_profile_url.split("?")[0] # we keep URI and remove URL parameters
    #             profile_id = extract_profile_id(raw_profile_url)

    #             add_profile_to_db(profile_id, profile_url)

    #             time.sleep(10)

    #         except Exception as e:
    #             traceback.print_exc()

    i = get_index()
    while True:
        
        try:

            print(i)
            root_profile_id = get_list_of_users_id()[i]

            raw_connex_profiles = request_profile_connex_profiles(root_profile_id)
            connex_profiles = extract_profiles_url(raw_connex_profiles)

            for profile in connex_profiles:
                if profile["id"] not in get_list_of_users_id():
                    add_profile_to_db(profile["id"], profile["url"])
                    time.sleep(10)

            i+=1
            update_index(i)

        except JSONDecodeError:
            time.sleep(10)

        except Exception as e:
            error_traceback = traceback.print_exc()
            notify_error(str(error_traceback))
            print(error_traceback)
            time.sleep(10)

