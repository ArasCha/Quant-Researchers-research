import requests
from dotenv import dotenv_values

li_at = dotenv_values(".env")["li_at"]
JSESSIONID = dotenv_values(".env")["JSESSIONID"]

headers = {
    "accept": "application/vnd.linkedin.normalized+json+2.1",
    "accept-language": "fr,fr-FR;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6",
    "csrf-token": f"{JSESSIONID}",
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
    url = f"https://www.linkedin.com/voyager/api/graphql?variables=(start:{page_number*page_limit},origin:FACETED_SEARCH,query:(keywords:quantitative,flagshipSearchIntent:SEARCH_SRP,queryParameters:List((key:geoUrn,value:List(90009659)),(key:industry,value:List(43)),(key:resultType,value:List(PEOPLE))),includeFiltersInResponse:false))&queryId=voyagerSearchDashClusters.37920f17209f22c510dd410658abc540"
    """Quants around Paris and in Financial Services"""

    request = requests.get(url, headers=headers)

    return request.json()


def request_profile_section(profile_id: str, section: str) -> dict:
    """
    Args:
        profile_id (str): id of the LinkedIn profile.
        section (str): education | certifications | experience.
    """

    url = f"https://www.linkedin.com/voyager/api/graphql?variables=(profileUrn:urn%3Ali%3Afsd_profile%3A{profile_id},sectionType:{section},locale:en_US)&queryId=voyagerIdentityDashProfileComponents.0aa4fe1d7819f1b21efc5be88cc3735d"

    request = requests.get(url, headers=headers)

    return request.json()


def request_profile_connex_profiles(profile_id: str) -> list[dict]:
    """
    Returns: list of 40 profiles relevant to a profile
    """

    # People you may know
    url_known = f"https://www.linkedin.com/voyager/api/graphql?variables=(profileUrn:urn%3Ali%3Afsd_profile%3A{profile_id})&queryId=voyagerIdentityDashProfileCards.7fdc5805f4be08bcc3a3577013d66d3d"
    request_known = requests.get(url_known, headers=headers)

    # More profiles for you
    url_more = f"https://www.linkedin.com/voyager/api/graphql?variables=(profileUrn:urn%3Ali%3Afsd_profile%3A{profile_id},sectionType:browsemap-recommendations)&queryId=voyagerIdentityDashProfileComponents.7f5e16224b53da3d4b722ed8f8f5fbf8"
    request_more = requests.get(url_more, headers=headers)

    content = request_known.json()
    content["included"].extend(request_more.json()["included"])

    return content["included"]


def notify_error(message: str):

    notifier_url = dotenv_values(".env")["NOTIFIER_URL"]
    auth = dotenv_values(".env")["NOTIFIER_AUTH"]

    headers = {
        "Content-Type": "application/json",
        "Accept-Charset": "utf-8"
    }
    data = {
        "message": message,
        "authorization": auth
    }

    response = requests.post(notifier_url, json=data, headers=headers)
