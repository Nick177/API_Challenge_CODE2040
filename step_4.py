import requests
import json

def removePrefix(token, toReceive, toSend) :
    ## Summary: Removes strings from a list with a certain prefix
    ## Precondition: Token key to make request, endpoint to grab dictionary with strings and prefix, endpoint to send result
    ## Postcondition: dictionary with list containing strings without prefix
    
    
    access_dict = dict()
    access_dict['token'] = token
    
    result_dict = dict()
    result_dict['token'] = access_dict['token']
    
    r = requests.post(toReceive, data=access_dict)
    
    d = dict()
    d = r.json()
    
    l = list()
    l = d['array']
    
    result = list()
    
    prefix = d['prefix']
    prefixLen = len(d['prefix'])
    
    ## Check which strings do not have prefix and add them to separate list
    for str in l :
        if(prefix != str[:prefixLen]) :
            result.append(str)
    
    ## Add list of strings without prefix to results dictionary
    result_dict['array'] = result
    
    r = requests.post(toSend, json=result_dict)
    
    print r.text

    print r.status_code  
    
    
    
token = '0613c21581d3243b69b6bab93e8f12bf'
toReceive = 'http://challenge.code2040.org/api/prefix'
toSend = 'http://challenge.code2040.org/api/prefix/validate'

removePrefix(token, toReceive, toSend)