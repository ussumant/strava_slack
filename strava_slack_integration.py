
# coding: utf-8

# In[ ]:

import urllib
import json
import requests
import time



def minute(s):  # converts to min:seconds format
    z= ((s- int(s))*60)/100
    return round((int(s)+z),2)
kk= requests.get("https://www.strava.com/api/v3/clubs/240555/activities", headers={ 'Authorization':' Bearer 4c1fd5abb6ca406b90ca5d0cf345c78ea69554d9'})
dta= json.loads(kk.text)    
    
dt= dta[0]['id']
dt=964443361
k=10

for i in range(k):
    r= requests.get("https://www.strava.com/api/v3/clubs/240555/activities", headers={ 'Authorization':' Bearer 4c1fd5abb6ca406b90ca5d0cf345c78ea69554d9'})
    data= json.loads(r.text)
    k=k+1
    if data[0]['id']==dt:
        print("same",dt)
        time.sleep(200);

    else:
        d= data[0]['id']
        print(dt)
        name= data[0]['athlete']['firstname']
        dist= round(((data[0]['distance'])/1000),2) # distance in km
        sped=1/((data[0]['average_speed'])*0.06)
        speed= minute(sped) # speed in min/km
        e= (data[0]['elapsed_time'])/60
        e_time= minute(e)# elapsed time in minutes
        webhook_url = "https://hooks.slack.com/services/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"
        slack_data = {"username": "Strava", "icon_emoji": ":runner:",
            "attachments": [
                {
                    "title": str(dist)+" km",
                    "pretext": name +" just went for a run!",
                    "text": "He _did it_ with a pace of *"+str(speed)+" min/km* with a total time of *"+str(e_time)+" minutes*",
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


