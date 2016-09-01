import requests ## to make a HTTP request to url
import json
import urllib ## used to help fetch url

"""
Step 1
"""
def connect(token, github_url) : 
    json_str = dict()
    json_str['token'] = token
    json_str['github'] = github_url

    endpoint_url = 'http://challenge.code2040.org/api/register'

    r = requests.post(endpoint_url, data=json_str)
    print r.text
    print r.status_code
    
    
##################################################
 ##       Main
 #################################################
token = '0613c21581d3243b69b6bab93e8f12bf'
github_url = 'https://github.com/Nick177/API_Challenge_CODE2040.git'

connect(token, github_url)