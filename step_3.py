import requests
import json
import urllib

def findNeedle(token):
    toReceive = 'http://challenge.code2040.org/api/haystack'
    toSend = 'http://challenge.code2040.org/api/haystack/validate'
    
    access_dict = dict() ## dictionary to access data
    result_dict = dict() ## dictionary to send result data
    
    access_dict['token'] = token
    
    r = requests.post(toReceive, data=access_dict)
    
    d = dict() ## temporary dictionary
    d = r.json() ## to receive dictionary from requests
    
    needle = d['needle']
    result_dict['token'] = access_dict['token']
    result_dict['needle'] = d['haystack'].index(needle)
    
    r = requests.post(toSend, data=result_dict)
    
    print r.text
    print r.status_code
    
    
    
    
######################################################
##                  Main                            ##
######################################################

token = '0613c21581d3243b69b6bab93e8f12bf'

findNeedle(token)