import re

def extract_profile_id(url: str) -> str:
    mini_profile_id = re.search(r'fs_miniProfile%3A([\w-]+)', url)
    if mini_profile_id:
        return mini_profile_id.group(1)
    else:
        raise Exception("Failed to extract profile id")
