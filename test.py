import json
import requests
from requests.auth import HTTPBasicAuth
commandList = ['1 - Status', '2 - Mission List', '3 - Add Mission to Queue']
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

if inputCommand == '3':
    inputMissionName = input('Please enter the mission name that you wish to add the queue:')
    r=requests.get('http://mir.com/api/v2.0.0/missions',
                    headers={"Authorization": "Basic %s" % 'YWRtaW46OGM2OTc2ZTViNTQxMDQxNWJkZTkwOGJkNGRlZTE1ZGZiMTY3YTljODczZmM0YmI4YTgxZjZmMmFiNDQ4YTkxOA=='})                
    dictData = json.loads(r.text)
    for dictObject in dictData:
        if inputMissionName == dictObject['name']:
            missionGuid = dictObject['guid']
            headers = {
                "Content-Type": "json",
                "Authorization": "Basic %s" % "YWRtaW46OGM2OTc2ZTViNTQxMDQxNWJkZTkwOGJkNGRlZTE1ZGZiMTY3YTljODczZmM0YmI4YTgxZjZmMmFiNDQ4YTkxOA=="
            }
            addNewMission=requests.post('http://mir.com/api/v2.0.0/mission_queue',
                                         headers=headers)
            print(addNewMission.text)

