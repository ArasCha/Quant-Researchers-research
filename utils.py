import re

def extract_profile_id(url: str) -> str:
    mini_profile_id = re.search(r'fs_miniProfile%3A([\w-]+)', url)
    if mini_profile_id:
        return mini_profile_id.group(1)
    else:

        raise Exception(f"Failed to extract profile id, url: {url}")


def extract_data_field(raw_field_data: dict) -> dict:

    elements_data = raw_field_data["included"][0]["components"]["elements"]
    
    final_elements = []

    for element in elements_data:

        title = element["components"]["entityComponent"]["titleV2"]["text"]["text"]
        
        try:
            subtitle = element["components"]["entityComponent"]["subtitle"]["text"]
        except:
            subtitle = None

        try:
            caption = element["components"]["entityComponent"]["caption"]["text"]
        except:
            caption = None

        final_elements.append({"title": title, "subtitle": subtitle, "caption": caption})

    return final_elements


def extract_education_data(raw_education_data: dict) -> dict:

    data = extract_data_field(raw_education_data)

    return [{"school": education["title"], "degree": education["subtitle"], "year": education["caption"]} for education in data]


def extract_certifications_data(raw_certification_data: dict) -> dict:

    try:
        data = extract_data_field(raw_certification_data)

        return [{"name": certif["title"], "institution": certif["subtitle"], "year": certif["caption"]} for certif in data]

    except TypeError:
        return None