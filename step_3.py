import requests ## To be able to make requests to URL
import json ## to work with json
#import urllib ## In association with making requests, but not necessary

def findNeedle(token):
    toReceive = 'http://challenge.code2040.org/api/haystack' ## URL to receive dictionary
    toSend = 'http://challenge.code2040.org/api/haystack/validate' ## URL to send result
    
    access_dict = dict() ## dictionary to access data
    result_dict = dict() ## dictionary to send result data
    
    access_dict['token'] = token
    
    r = requests.post(toReceive, data=access_dict) ## Make request to endpoint for dictionary
    
    d = dict() ## temporary dictionary
    d = r.json() ## to place dictionary from requests
    
    ##Finds the needle, then stores the index in the result dictionary along with the token
    needle = d['needle']
    result_dict['token'] = access_dict['token']
    result_dict['needle'] = d['haystack'].index(needle)
    
    r = requests.post(toSend, data=result_dict) ## Make request with our results
    
    ## print out result message for (pass/fail)
    print r.text
    print r.status_code
    
    
    
    
######################################################
##                  Main                            ##
######################################################

token = '0613c21581d3243b69b6bab93e8f12bf'

findNeedle(token)