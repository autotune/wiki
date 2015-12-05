#!/usr/bin/python2.7
import requests

txt=open("token.txt")
token=txt.read()
event_id='19829420330/'
events_endpoint="https://www.eventbriteapi.com/v3/events/" + event_id
user_endpoint="https://www.eventbriteapi.com/v3/users/me/"

response = requests.get(
    events_endpoint, 

    headers = {
        "Authorization": "Bearer %s" % (token)
    },
    verify = True,  # Verify SSL certificate
)

print response.json() 
