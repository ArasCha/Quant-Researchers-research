import re


def extract_profile_id(url: str) -> str:
    mini_profile_id = re.search(r'fs_miniProfile%3A([\w-]+)', url)
    if mini_profile_id:
        return mini_profile_id.group(1)
    else:

        raise Exception(f"Failed to extract profile id, url: {url}")


def extract_data(raw_data: dict, result_format: dict) -> dict:
    """
    Args:
        raw_data (dict): raw JSON data resulting from a GET request on https://www.linkedin.com/voyager/api/graphql?variables=...
        result_format (dict): format wished mapping the raw data fields. Example: {"job":"titleV2", "company": "subtitle", "date": "caption", "location": "metadata"}
    """

    final_elements = []

    for element in raw_data["included"][0]["components"]["elements"]:

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
