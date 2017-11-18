
# coding: utf-8

# In[ ]:

import urllib
import json
import requests
import time



def minute(s):  # converts to min:seconds format
    z= ((s- int(s))*60)/100
    return round((int(s)+z),2)
kk= requests.get("https://www.strava.com/api/v3/clubs/240555/activities", headers={ 'Authorization':' Bearer <API KEY STRAVA>'})
dta= json.loads(kk.text)    
    
#dt= dta[0]['id']
text_file = open("Output.txt", "r")
dt=int(text_file.read())
#text_file.close()

k=10

for i in range(k):
    r= requests.get("https://www.strava.com/api/v3/clubs/240555/activities", headers={ 'Authorization':' Bearer <API KEY STRAVA>'})
    data= json.loads(r.text)
    k=k+1
    if data[0]['id']==dt:
        print("same",dt)
        time.sleep(1000);

    else:
        d= data[0]['id']
        print(dt)
        name= data[0]['athlete']['firstname']
        sex= data[0]['athlete']['sex']
        dist= round(((data[0]['distance'])/1000),2) # distance in km
        sped=1/((data[0]['average_speed'])*0.06)
        speed= minute(sped) # speed in min/km
        e= (data[0]['elapsed_time'])/60
        e_time= minute(e)# elapsed time in minutes
        webhook_url = "<SLACK WEBHOOK>"
        if sex=='M':
            slack_data = {"username": "Strava", "icon_emoji": ":runner:",
                "attachments": [
                    {
                        "title": str(dist)+" km",
                        "pretext": name +" just went for a run!",
                        "text": "He did it with a pace of *"+str(speed)+" min/km* with a total time of *"+str(e_time)+" minutes*",
                        "mrkdwn_in": [
                            "text",
                            "pretext"
                        ]
                    }
                ]
            }
        else:
            slack_data = {"username": "Strava", "icon_emoji": ":runner:",
                "attachments": [
                    {
                        "title": str(dist)+" km",
                        "pretext": name +" just went for a run!",
                        "text": "She did it with a pace of *"+str(speed)+" min/km* with a total time of *"+str(e_time)+" minutes*",
                        "mrkdwn_in": [
                            "text",
                            "pretext"
                        ]
                    }
                ]
            }

        response = requests.post(
            webhook_url, data=json.dumps(slack_data),
            headers={'Content-Type': 'application/json'}
        )
        dt= data[0]['id']
        print("new", dt)
        text_file = open("Output.txt", "w")
        text_file.write(str(dt))
        text_file.close()


