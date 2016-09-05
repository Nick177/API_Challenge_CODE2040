import requests
import json
import urllib

def getDateAndInterval(token) :
    
    access_dict = dict()
    access_dict['token'] = token
    toReceive = 'http://challenge.code2040.org/api/dating'
    
    r = requests.post(toReceive, data=access_dict)
        
    return r.json()
    
def calcDate(date, interval) :
    t_mo_index = date.index('-') + 4
    t_d_index = date.index('T') - 2
    t_h_index = date.index('T') + 1
    t_m_index = t_h_index + 3
    t_s_index = t_m_index + 3
    
    
    cur_secs = int(date[t_s_index:t_s_index+2])
    cur_mins = int(date[t_m_index:t_m_index+2])
    cur_hours = int(date[t_h_index:t_h_index+2])
    cur_days = int(date[t_d_index:t_d_index+2])
    cur_month = int(date[t_mo_index:t_mo_index+2])
        
    extra_mins = int(interval / 60) ## Simplify the seconds given to minutes, (called extra because it will be added to current mins)
    extra_secs = int(interval % 60)  ## This will get any seconds left over that do not fit into minutes
    extra_hours = int(extra_mins / 60) ## Out of the extra minutes, cuts it down to how many hours it makes up
    extra_mins = int(extra_mins % 60) ## After converting mins to hours, this will get left over mins
    extra_days = int(extra_hours / 24) ## Gets how many days the extra hours can make up (if any)
    extra_hours = int(extra_hours % 24) ## Saves the left over hours not converted to days
        
    ## Add together
    cur_secs = cur_secs + extra_secs
    leftOver = int(cur_secs / 60)
    if(leftOver != 0) :
        cur_secs = cur_secs % 60
    
    
    cur_mins = cur_mins + extra_mins + leftOver
    leftOver = int(cur_mins / 60)
    if(leftOver != 0) :
        cur_mins = cur_mins % 60
    
    
    cur_hours = cur_hours + extra_hours + leftOver
    leftOver = int(cur_hours / 24)
    if(leftOver != 0) :
        cur_hours = cur_hours % 24
        
    cur_days = cur_days + extra_days + leftOver
        
    if(cur_days < 10) :
        date = date[:t_mo_index] + '0' + str(cur_days) + date[t_mo_index+2:]
    else :
        date = date[:t_mo_index] + str(cur_days) + date[t_mo_index+2:]

    if(cur_hours < 10) :
        date = date[:t_h_index] + '0' + str(cur_hours) + date[t_h_index+2:]
    else :
        date = date[:t_h_index] + str(cur_hours) + date[t_h_index+2:]
    if(cur_mins < 10) : 
        date = date[:t_m_index] + '0' + str(cur_mins) + date[t_m_index+2:]
    else :
        date = date[:t_m_index] + str(cur_mins) + date[t_m_index+2:]
    if(cur_secs < 10) :
        date = date[:t_s_index] + '0' + str(cur_secs) + date[t_s_index+2:]
    else :
        date = date[:t_s_index] + str(cur_secs) + date[t_s_index+2:]
            
    return date
    
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