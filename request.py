import requests
from dotenv import dotenv_values

li_at = dotenv_values(".env")["li_at"]
JSESSIONID = dotenv_values(".env")["JSESSIONID"]


def request_profiles(page_number: int) -> dict:
    
    page_limit = 10
    url = f"https://www.linkedin.com/voyager/api/graphql?variables=(start:{page_number*page_limit},origin:SWITCH_SEARCH_VERTICAL,query:(keywords:data%20scientist,flagshipSearchIntent:SEARCH_SRP,queryParameters:List((key:currentCompany,value:List(1586,1441,10667,162479,165158)),(key:resultType,value:List(PEOPLE))),includeFiltersInResponse:false))&queryId=voyagerSearchDashClusters.bfece70e8e0c145475cc058fe06aa02f"
    
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
        "Referer": "https://www.linkedin.com/search/results/people/?currentCompany=%5B%221586%22%2C%221441%22%2C%2210667%22%2C%22162479%22%2C%22165158%22%5D&keywords=data%20scientist&origin=FACETED_SEARCH&sid=qb%40",
        "Referrer-Policy": "strict-origin-when-cross-origin"
  }

    request = requests.get(url, headers=headers)

    return request.json()

# fetch("https://www.linkedin.com/voyager/api/graphql?variables=(start:10,origin:FACETED_SEARCH,query:(keywords:data%20scientist,flagshipSearchIntent:SEARCH_SRP,queryParameters:List((key:currentCompany,value:List(1586,1441,10667,162479,165158)),(key:resultType,value:List(PEOPLE))),includeFiltersInResponse:false))&queryId=voyagerSearchDashClusters.bfece70e8e0c145475cc058fe06aa02f", {
#   "headers": {
#     "accept": "application/vnd.linkedin.normalized+json+2.1",
#     "accept-language": "fr,fr-FR;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6",
#     "csrf-token": "ajax:6530702647513887698",
#     "priority": "u=1, i",
#     "sec-ch-ua": "\"Chromium\";v=\"124\", \"Microsoft Edge\";v=\"124\", \"Not-A.Brand\";v=\"99\"",
#     "sec-ch-ua-mobile": "?0",
#     "sec-ch-ua-platform": "\"Windows\"",
#     "sec-fetch-dest": "empty",
#     "sec-fetch-mode": "cors",
#     "sec-fetch-site": "same-origin",
#     "x-li-lang": "en_US",
#     "x-li-page-instance": "urn:li:page:d_flagship3_search_srp_people_load_more;Jl1bFfFMR02ve30QD8BDlA==",
#     "x-li-pem-metadata": "Voyager - People SRP=search-results",
#     "x-li-track": "{\"clientVersion\":\"1.13.15893\",\"mpVersion\":\"1.13.15893\",\"osName\":\"web\",\"timezoneOffset\":2,\"timezone\":\"Europe/Paris\",\"deviceFormFactor\":\"DESKTOP\",\"mpName\":\"voyager-web\",\"displayDensity\":1.2000000476837158,\"displayWidth\":1920.0000762939453,\"displayHeight\":1080.0000429153442}",
#     "x-restli-protocol-version": "2.0.0"
#   },
#   "referrer": "",
#   "referrerPolicy": "strict-origin-when-cross-origin",
#   "body": null,
#   "method": "GET",
#   "mode": "cors",
#   "credentials": "include"
# });

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