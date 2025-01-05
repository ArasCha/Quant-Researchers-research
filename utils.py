import re


def extract_profile_id(url: str) -> str:
    mini_profile_id = re.search(r'fs_miniProfile%3A([\w-]+)', url)
    if mini_profile_id:
        return mini_profile_id.group(1)
    else:

        raise Exception(f"Failed to extract profile id, url: {url}")


def extract_data(raw_data: dict, result_format: dict) -> list:
    """
    Args:
        raw_data (dict): raw JSON data resulting from a GET request on https://www.linkedin.com/voyager/api/graphql?variables=...
        result_format (dict): format wished mapping the raw data fields. Example: {"job":"titleV2", "company": "subtitle", "date": "caption", "location": "metadata"}
    """

    final_elements = []

    try:
        elements = raw_data["included"][0]["components"]["elements"]
    except IndexError:
        return []

    for element in elements:

        element_data = result_format.copy()

        for field_name in element_data.keys():
            
            try:
                field_value = element["components"]["entityComponent"][element_data[field_name]]["text"]
                if type(field_value) is not str: field_value = field_value["text"]
            except TypeError:
                field_value = None

            element_data[field_name] = field_value

        final_elements.append(element_data)

    return final_elements


def extract_projects(raw_data: dict) -> dict:

    final_elements = []

    i=0
    while True:
        try:
            elements = raw_data["included"][i]["components"]["elements"]
            break
        except KeyError:
            i+=1
        except IndexError:
            return []

    for project_data in elements:

        try:
            title = project_data["components"]["entityComponent"]["titleV2"]["text"]["text"]
        except TypeError:
            return final_elements
        try:
            institution = project_data["components"]["entityComponent"]["subComponents"]["components"][0]["components"]["insightComponent"]["text"]["text"]["text"]
        except TypeError:
            institution = None
        try:
            link = project_data["components"]["entityComponent"]["subComponents"]["components"][1]["components"]["actionComponent"]["action"]["navigationAction"]["actionTargetV2"]["deeplink"]
        except:
            link = None
        try:
            date = project_data["components"]["entityComponent"]["subtitle"]["text"]
        except TypeError:
            date = None
        
        final_elements.append({
            "title": title,
            "institution": institution,
            "link": link,
            "date": date
        })

    return final_elements


def extract_profiles_url(raw_data: dict) -> list[dict]:

    profiles_url = []

    for element in raw_data["included"]:
        try:
            profiles_url.append({
                "url": f"https://www.linkedin.com/in/{element['publicIdentifier']}",
                "id": element['entityUrn'].split(":")[3]
                })
        except KeyError:
            pass

    return profiles_url