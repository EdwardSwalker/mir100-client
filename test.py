import requests
from requests.auth import HTTPBasicAuth
inputCommand = input('Enter your name:')
print('Hello, ' + inputCommand)
r=requests.post('http://mir.com/api/v2.0.0/missions',
                headers={"Authorization": "Basic %s" % 'YWRtaW46OGM2OTc2ZTViNTQxMDQxNWJkZTkwOGJkNGRlZTE1ZGZiMTY3YTljODczZmM0YmI4YTgxZjZmMmFiNDQ4YTkxOA=='})