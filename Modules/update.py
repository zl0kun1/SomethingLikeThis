# Auto Almost Everything
# Youtube Channel https://www.youtube.com/c/AutoAlmostEverything
# Please read README.md carefully before use

import requests

current_version_tag = 'v1.4b'


def check():
    new_version_tag = requests.get(
        'https://raw.githubusercontent.com/autoalmosteverything/PreSearch/main/RELEASE.md').text
    if new_version_tag != current_version_tag:
        return True
    return False
