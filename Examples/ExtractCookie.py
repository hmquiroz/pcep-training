import requests

resp = requests.get("https://bcp-ti.atlassian.net/jira/software/c/projects/COPH/boards/2441") # not login as user
#resp = requests.get("https://github.com") # not login as user

cookies = resp.cookies
for cookie in cookies:
    print(cookie.name, cookie.value)
