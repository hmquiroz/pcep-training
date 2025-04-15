import requests
response = session.get('http://google.com')
print(session.cookies.get_dict())