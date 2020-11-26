import json
import requests
from requests.auth import HTTPBasicAuth
commandList = ['1 - Status', '2 - Mission List']
print(*commandList, sep='\n')
inputCommand = input('Please enter command number:')
print('Running' + ' ' + commandList[int(inputCommand) - 1] + '...' + '\n')

if inputCommand == '1':
    r=requests.get('http://mir.com/api/v2.0.0/status',
                    headers={"Authorization": "Basic %s" % 'YWRtaW46OGM2OTc2ZTViNTQxMDQxNWJkZTkwOGJkNGRlZTE1ZGZiMTY3YTljODczZmM0YmI4YTgxZjZmMmFiNDQ4YTkxOA=='})
    print(r.text)
# r=requests.post('http://mir.com/api/v2.0.0/missions',
# headers={"Authorization": "Basic %s" % 'YWRtaW46OGM2OTc2ZTViNTQxMDQxNWJkZTkwOGJkNGRlZTE1ZGZiMTY3YTljODczZmM0YmI4YTgxZjZmMmFiNDQ4YTkxOA=='})
if inputCommand == '2':
    r=requests.get('http://mir.com/api/v2.0.0/missions',
                    headers={"Authorization": "Basic %s" % 'YWRtaW46OGM2OTc2ZTViNTQxMDQxNWJkZTkwOGJkNGRlZTE1ZGZiMTY3YTljODczZmM0YmI4YTgxZjZmMmFiNDQ4YTkxOA=='})                
    dictData = json.loads(r.text)
    for dictObject in dictData:
        print(dictObject['name'])

