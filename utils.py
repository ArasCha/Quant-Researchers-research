import re

def extract_profile_id(url:str):
    try:
        mini_profile_id = re.search(r'fs_miniProfile%3A([\w-]+)', url)
        if mini_profile_id:
            return mini_profile_id.group(1)
        else:
            print("Failed to extract profile id")
    except Exception as e:
        print("An error occurred:", str(e))
    return None