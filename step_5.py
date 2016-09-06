import requests
import json
import datetime ## Module that has built in functions to cut down conversion and calculation

def getDateAndInterval(token) :
    
    access_dict = dict()
    access_dict['token'] = token
    toReceive = 'http://challenge.code2040.org/api/dating'
    
    r = requests.post(toReceive, data=access_dict)
        
    return r.json()
    
def calcDate(date, interval) :
    
    ## make a datetime object from string given
    date = datetime.datetime.strptime(date, "%Y-%m-%dT%H:%M:%SZ")
    ## Add the seconds (interval) to the date
    date = date + datetime.timedelta(seconds=interval)
    ## Added character 'Z' at the end due to isoformat() function leaving it out
    return date.isoformat() + 'Z'
    
    
def sendDate(token, endpoint, date) :
    access_dict = dict()
    access_dict['token'] = token
    access_dict['datestamp'] = date

    r = requests.post(endpoint, data=access_dict)
    
    print r.text
    print r.status_code
    

token = '0613c21581d3243b69b6bab93e8f12bf'
endpoint = 'http://challenge.code2040.org/api/dating/validate'


temp_dict = dict()
temp_dict = getDateAndInterval(token)

time_str = str(temp_dict['datestamp'])
interval = temp_dict['interval']

#time_str = '2016-09-11T12:47:54Z'
#interval = 172736

date = calcDate(time_str, interval)

sendDate(token, endpoint, date)

##addInterval(x)