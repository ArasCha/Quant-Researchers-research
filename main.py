from request import request_profiles, request_profile_section
from utils import extract_profile_id, extract_data
from db import insert_data
import time
import traceback



if __name__ == "__main__":

    for page_number in range(100): # only 100 pages maximum

        data = request_profiles(page_number)

        profiles = data["included"]

        for profile in profiles:
            try:
                raw_profile_url: str = profile["navigationUrl"]
                profile_url = raw_profile_url.split("?")[0] # we keep URI and remove URL parameters
                
                profile_id = extract_profile_id(raw_profile_url)

                raw_education_data = request_profile_section(profile_id, "education")
                raw_experience_data = request_profile_section(profile_id, "experience")
                
                print(profile_url)
                insert_data({
                    "profile_url": profile_url,
                    "education": extract_data(raw_education_data,
                        {   "school":"titleV2",
                            "degree":"subtitle",
                            "year": "caption"
                        }),
                    "experience": extract_data(raw_experience_data,
                        {   "job":"titleV2",
                            "company": "subtitle",
                            "date": "caption",
                            "location": "metadata"
                        })
                    })

                time.sleep(10)

            except KeyError as e: # a bunch of irrelevant data will be in data. If it doesn't have the navigationUrl attribute we'll assume it's not a profile
                pass

            except Exception as e:
                traceback.print_exc()

