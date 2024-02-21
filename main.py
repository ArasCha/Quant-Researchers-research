from request import request_profiles, request_education
from utils import extract_profile_id
from db import db
import time

if __name__ == "__main__":

    for page_number in range(100): # only 100 pages maximum

        data = request_profiles(page_number)

        profiles = data["included"]

        for profile in profiles:
            try:
                raw_profile_url: str = profile["navigationUrl"]
                profile_url = raw_profile_url.split("?")[0] # we keep URI and remove URL parameters
                
                profile_id = extract_profile_id(raw_profile_url)

                data = request_education(profile_id)
                education_data = data["included"][0]["components"]["elements"]

                education_total = []

                for education in education_data:

                    school = education["components"]["entityComponent"]["titleV2"]["text"]["text"]
                    
                    try:
                        degree = education["components"]["entityComponent"]["subtitle"]["text"]
                    except:
                        degree = None

                    education_total.append({"school": school, "degree": degree})
                
                quant_researchers = db.quant_researchers
                quant_researchers.insert_one({"profile_url": profile_url, "education": education_total})
                print(profile_url)

                time.sleep(10)

            except Exception as e: # a bunch of irrelevant data will be in data. If it doesn't have the navigationUrl attribute we'll assume it's not a profile
                if profile["entityUrn"]: # it's normal to have this entityUrn attribute
                    pass
                else:
                    print("Weird:", str(e))
