import requests
from dotenv import dotenv_values

li_at = dotenv_values(".env")["li_at"]
JSESSIONID = dotenv_values(".env")["JSESSIONID"]


def request_profiles(page_number: int) -> dict:
    
    page_limit = 10
    url = f"https://www.linkedin.com/voyager/api/graphql?variables=(start:{page_number*page_limit},origin:SWITCH_SEARCH_VERTICAL,query:(keywords:quantitative%20researcher,flagshipSearchIntent:SEARCH_SRP,queryParameters:List((key:resultType,value:List(PEOPLE))),includeFiltersInResponse:false))&queryId=voyagerSearchDashClusters.ecc0d60fe98848da4adc6b796a441f55"
    
    headers = {
        "accept": "application/vnd.linkedin.normalized+json+2.1",
        "accept-language": "fr,fr-FR;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6",
        "csrf-token": "ajax:1660307672432702115",
        "sec-ch-ua": "\"Not A(Brand\";v=\"99\", \"Microsoft Edge\";v=\"121\", \"Chromium\";v=\"121\"",
        "sec-ch-ua-mobile": "?0",
        "sec-ch-ua-platform": "\"Windows\"",
        "sec-fetch-dest": "empty",
        "sec-fetch-mode": "cors",
        "sec-fetch-site": "same-origin",
        "x-li-lang": "en_US",
        "x-li-page-instance": "urn:li:page:d_flagship3_search_srp_people_load_more;jqgyh4YwQLKqKrONRU7P0g==",
        "x-li-pem-metadata": "Voyager - People SRP=search-results",
        "x-li-track": "{\"clientVersion\":\"1.13.10680\",\"mpVersion\":\"1.13.10680\",\"osName\":\"web\",\"timezoneOffset\":1,\"timezone\":\"Europe/Paris\",\"deviceFormFactor\":\"DESKTOP\",\"mpName\":\"voyager-web\",\"displayDensity\":1,\"displayWidth\":1920,\"displayHeight\":1080}",
        "x-restli-protocol-version": "2.0.0",
        "cookie": f"li_at={li_at}; JSESSIONID=\"{JSESSIONID}\"",
        "Referer": "https://www.linkedin.com/search/results/people/?keywords=quantitative%20researcher&origin=SWITCH_SEARCH_VERTICAL&sid=t.O",
        "Referrer-Policy": "strict-origin-when-cross-origin"
  }

    request = requests.get(url, headers=headers)

    return request.json()


def request_education(profile_id:str) -> dict:

    url = f"https://www.linkedin.com/voyager/api/graphql?includeWebMetadata=true&variables=(profileUrn:urn%3Ali%3Afsd_profile%3A{profile_id},sectionType:education,locale:en_US)&queryId=voyagerIdentityDashProfileComponents.0aa4fe1d7819f1b21efc5be88cc3735d"

    headers = {
        "accept": "application/vnd.linkedin.normalized+json+2.1",
        "accept-language": "fr,fr-FR;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6",
        "csrf-token": "ajax:1660307672432702115",
        "sec-ch-ua": "\"Not A(Brand\";v=\"99\", \"Microsoft Edge\";v=\"121\", \"Chromium\";v=\"121\"",
        "sec-ch-ua-mobile": "?0",
        "sec-ch-ua-platform": "\"Windows\"",
        "sec-fetch-dest": "empty",
        "sec-fetch-mode": "cors",
        "sec-fetch-site": "same-origin",
        "x-li-lang": "en_US",
        "x-li-page-instance": "urn:li:page:d_flagship3_profile_view_base_education_details;07+/PinxQiOtxFjSlfOYxg==",
        "x-li-pem-metadata": "Voyager - Profile=view-education-details",
        "x-li-track": "{\"clientVersion\":\"1.13.10680\",\"mpVersion\":\"1.13.10680\",\"osName\":\"web\",\"timezoneOffset\":1,\"timezone\":\"Europe/Paris\",\"deviceFormFactor\":\"DESKTOP\",\"mpName\":\"voyager-web\",\"displayDensity\":1,\"displayWidth\":1920,\"displayHeight\":1080}",
        "x-restli-protocol-version": "2.0.0",
        "cookie": f"li_at={li_at}; JSESSIONID=\"{JSESSIONID}\"",
        "Referer": "https://www.linkedin.com",
        "Referrer-Policy": "strict-origin-when-cross-origin"
  }

    request = requests.get(url, headers=headers)

    return request.json()