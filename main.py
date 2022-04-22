import linecache
import winsound
import requests
import json
import os
from time import sleep as sleep
import linecache
from datetime import datetime
from datetime import date
def cls():
    os.system('cls' if os.name=='nt' else 'clear')

curdir = os.getcwd()
if os.path.exists('config.txt'):
    print('config was found!')
else:
    print('The "config.txt file could not be found. please check if it is named correctly.')
    sleep (5)
    quit()
userid = linecache.getline('config.txt', 3).strip()   #strip is needed because of diz stupid newline at end of getline lines
notifsettingstatus = linecache.getline('config.txt', 2).strip()
reqinterval =linecache.getline('config.txt', 1).strip()
logsetting = linecache.getline('config.txt', 4).strip()
Minsetting = linecache.getline('config.txt', 5).strip()
WebHookLink = linecache.getline('config.txt', 6).strip()
WebHookSetting = linecache.getline('config.txt', 7).strip()

roblox_api_statusresponse=requests.get('https://api.roblox.com/users/'+userid+'/')
roblox_api_statustext = roblox_api_statusresponse.text
rolobx_api_statusjson = json.loads(roblox_api_statustext)
username = rolobx_api_statusjson['Username']

if os.path.exists(curdir+'/logs'): #checks for the folder "logs", if not found it will create one
    print('logs folder was found!')
    cls()
    pass
else:
    print('The logs folder could not be found. Creating one...')
    os.mkdir(curdir+'/logs')
    sleep(1)
    print('Folder "logs" has been created. continuing... (If you see this message on next start, please make an issue on github)')
    sleep(3)
    cls()
webhooksendstatus = 0 
diswebholdstatus = 0


















while 1 != 3:
    cls()
    roblox_api_requestdata = requests.get('https://api.roblox.com/users/'+ userid+'/onlinestatus/')
    roblox_api_requesttext = roblox_api_requestdata.text
    roblox_api_requestjson = json.loads(roblox_api_requesttext)
    online_status = roblox_api_requestjson['IsOnline']
    PresenceType = roblox_api_requestjson['PresenceType']
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    todaydate = date.today()
    if PresenceType == 2 and online_status==True:
        logstatus = 'is   <<<ONLINE>>>'
        diswebhcurstatus = 1
    else:
        logstatus = ('is   ---OFFLINE---   (PresenceType = '+str(PresenceType)+')')
        diswebhcurstatus = 0
    messagge =('Date: '+ str(todaydate) + '   '+'Time: '+str(current_time)+'   '+'Id: '+str(userid)+ ' '+ str(logstatus)+ '\n')
    msg = messagge
    if logsetting == 'True':
        file = open(curdir+'/logs/'+'log_'+ userid+'_'+username+'.txt','a')
        if Minsetting == 'True':
            file.write(str(todaydate) + '   '+str(current_time)+'   '+str(userid)+ ' '+ str(logstatus)+ '\n')
            file.close
        else:
            file.write(messagge)
            file.close
    else:
        pass
    
    if WebHookSetting == 'True':
            
            if diswebhcurstatus !=  diswebholdstatus:

            
                url = WebHookLink
            
                usrname = 'roblox_statustracker_bot'

                embed = {
                "description": "",
                "title": ""
                }

                data = {
                "content": messagge,
                "username": usrname,
    
                }

                headers = {
                "Content-Type": "application/json"
                }
            
                result = requests.post(url, json=data, headers=headers)
                if 200 <= result.status_code < 300:
                    pass
                
                else:
                    print(f"Not sent with {result.status_code}, response:\n{result.json()}")
                    
                diswebholdstatus = diswebhcurstatus
    
    
    
    
    if PresenceType == 2 and online_status==True:
        print('roblox id ['+userid+'] is ONLINE with username ['+str(username)+']')
        if notifsettingstatus == 'True':
            winsound.Beep(440, 250)
        else:
            pass
        
       

            
    else:
        
        print('roblox id ['+userid+'] is NOT ONLINE (username = '+str(username)+') (PresenceType = '+str(PresenceType)+')')
    sleep(float(reqinterval))
        
    