#!/usr/bin/python2.7
import requests
response = requests.get(
   "http://www.evbdev.com/ebapi/v3/users/me/owned_events",
   headers = {
       "Authorization": "Bearer:  
