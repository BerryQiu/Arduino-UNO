import requests
import json
import sys
import random
import time
import serial


def Get_Nowtemp():
    global now_temp
    response = str(ser.readline().decode())
    if response.startswith('N'):
        now_temp = response.lstrip('N')
    return now_temp


def Get_Settemp():
    global set_temp
    set_temp = '0'
    response = str(ser.readline().decode())
    if response.startswith('S'):
        set_temp = response.lstrip('S')
    return set_temp


def Up_temp1():
    nt = Get_Nowtemp()
    if sys.getdefaultencoding() != defaultencoding:
        reload(sys)
        sys.setdefaultencoding(defaultencoding)
    # 设备ID
    DEVICEID = '505210830'
    # 数据流名称
    SENSORID = 'Humidity'
    # 数值
    VALUE = nt
    # APIKEY
    APIKEY = 'P1SqxBIS5tO6ilhRp5Xnd=jZtOg='
    url = 'http://api.heclouds.com/devices/%s/datapoints' % (DEVICEID)
    print(url)
    dict = {"datastreams": [{"id": "temp", "datapoints": [{"value": 50}]}]}
    dict['datastreams'][0]['id'] = SENSORID
    dict['datastreams'][0]['datapoints'][0]['value'] = VALUE
    print(dict)
    s = json.dumps(dict)
    headers = {
        "api-key": APIKEY,
        "Connection": "close"
    }
    r = requests.post(url, headers=headers, data=s)
    print(r.headers)
    print('1', 20 * '*')
    print(r.text)
    print('2', 20 * '*')


def Up_temp2():
    st = Get_Settemp()
    if sys.getdefaultencoding() != defaultencoding:
        reload(sys)
        sys.setdefaultencoding(defaultencoding)
    # 设备ID
    DEVICEID = '505210830'
    # 数据流名称
    SENSORID = 'Light'
    # 数值
    VALUE = st
    # APIKEY
    APIKEY = 'P1SqxBIS5tO6ilhRp5Xnd=jZtOg='
    url = 'http://api.heclouds.com/devices/%s/datapoints' % (DEVICEID)
    print(url)
    dict = {"datastreams": [{"id": "temp", "datapoints": [{"value": 50}]}]}
    dict['datastreams'][0]['id'] = SENSORID
    dict['datastreams'][0]['datapoints'][0]['value'] = VALUE
    print(dict)
    s = json.dumps(dict)
    headers = {
        "api-key": APIKEY,
        "Connection": "close"
    }
    r = requests.post(url, headers=headers, data=s)
    print(r.headers)
    print('1', 20 * '*')
    print(r.text)
    print('2', 20 * '*')

defaultencoding = 'utf-8'
now_temp = '0'
set_temp = '0'

ser = serial.Serial('com3',9600)
while(1):
    Up_temp1()
    Up_temp2()
    time.sleep(5)


