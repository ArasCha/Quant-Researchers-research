import requests
from dotenv import dotenv_values

li_at = dotenv_values(".env")["li_at"]
JSESSIONID = dotenv_values(".env")["JSESSIONID"]

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
    "Referer": "https://www.linkedin.com/search/results/people/?industry=%5B%2246%22%2C%2243%22%2C%22129%22%2C%2245%22%5D&keywords=quantitative%20researcher%20trader&origin=FACETED_SEARCH&sid=w%3Aq",
    "Referrer-Policy": "strict-origin-when-cross-origin"
}


def request_profiles(page_number: int) -> dict:
    
    page_limit = 10
    url = f"https://www.linkedin.com/voyager/api/graphql?variables=(start:{page_number*page_limit},origin:SWITCH_SEARCH_VERTICAL,query:(keywords:quantitative%20researcher%20trader,flagshipSearchIntent:SEARCH_SRP,queryParameters:List((key:industry,value:List(46,43,129,45)),(key:resultType,value:List(PEOPLE))),includeFiltersInResponse:false))&queryId=voyagerSearchDashClusters.fd30e58dee57533de461750d523c4d31"
    
    request = requests.get(url, headers=headers)

    return request.json()


def request_education(profile_id:str) -> dict:

    url = f"https://www.linkedin.com/voyager/api/graphql?includeWebMetadata=true&variables=(profileUrn:urn%3Ali%3Afsd_profile%3A{profile_id},sectionType:education,locale:en_US)&queryId=voyagerIdentityDashProfileComponents.0aa4fe1d7819f1b21efc5be88cc3735d"

    request = requests.get(url, headers=headers)

    return request.json()


def request_certifications(profile_id:str) -> dict:

    url = f"https://www.linkedin.com/voyager/api/graphql?variables=(profileUrn:urn%3Ali%3Afsd_profile%3A{profile_id},sectionType:certifications,locale:en_US)&queryId=voyagerIdentityDashProfileComponents.34c38eb036e24f42647c693a62c45fbd"

    request = requests.get(url, headers=headers)

    return request.json()
