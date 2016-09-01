import requests
import urllib
import json

def reverseAndSend(token) :
    #Summary: Function sends a reversed string with HTTP Request
    #Precondition: Needs a token to access the string using a HTTP request and to send using a HTTP request
    #Postcondition: Reverses the string gained from first HTTP reqest to the endpoint and sends it with another
    #                HTTP request with the toSend link.
    
    endpoint1 = 'http://challenge.code2040.org/api/reverse'
    toSend = 'http://challenge.code2040.org/api/reverse/validate'
    json_str = dict()
    json_str['token'] = token
    
    r = requests.post(endpoint1, data=json_str)
    
    json_dic = dict()
    json_dic['token'] = token
    
    result = str(r.text)
    
    json_dic['string'] = result[::-1]
    
    r = requests.post(toSend, data = json_dic)
    print r.text
    print r.status_code


    
    
######################################################
##                  Main                            ##
######################################################

token = '0613c21581d3243b69b6bab93e8f12bf'

reverseAndSend(token)