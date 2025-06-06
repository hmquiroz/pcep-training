import requests

resp = requests.get("https://bcp-ti.atlassian.net/browse/COPH-14583") # not login as user
#resp = requests.get("https://github.com") # not login as user

cookies = resp.cookies
for cookie in cookies:
    print(cookie.name, cookie.value)
