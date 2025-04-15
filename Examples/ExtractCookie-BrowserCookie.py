#import browser_cookie3
#import requests

#url = "https://bcp-ti.atlassian.net/jira/software/c/projects/COPH/boards/2441?quickFilter=71594py"
#cj = browser_cookie3.chrome(domain_name='www.bitbucket.com')
#r = requests.get(url, cookies=cj)
#print(r.content)

import browser_cookie3,re
import requests

url="https://bcp-ti.atlassian.net/browse/OCD-98708"
cj = browser_cookie3.chrome(domain_name='https://bcp-ti.atlassian.net/browse/OCD-98708')
cookies = str(cj)
r = requests.get(url, cookies=cj)
cookielist = cookies.split(",")
print(cookielist)
#print(r.content)
for elem in cookielist:
    print(elem)
    mycook = re.search(r'tenant.session.token',elem)
    if mycook:
        thiselem = str(elem)
        print(re.search(r'<Cookie (.+?)for \.nseindia\.com', thiselem).group(1))