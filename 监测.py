import itchat
import requests
import json
import time
import serial
import re


ser2 = serial.Serial('com3',9600)


def num():
    # 基本设置

    url = "http://api.heclouds.com/devices/505210830/datastreams/Humidity"

    API_KEY = "P1SqxBIS5tO6ilhRp5Xnd=jZtOg="

    headers = {'api-key': API_KEY}


    r2 = requests.get(url, headers=headers)

    nt = json.loads(r2.content.decode('utf-8'))['data']['current_value']

    url = "http://api.heclouds.com/devices/505210830/datastreams/Light"

    API_KEY = "P1SqxBIS5tO6ilhRp5Xnd=jZtOg="

    headers = {'api-key': API_KEY}


    r1 = requests.get(url, headers=headers)

    st = json.loads(r1.content.decode('utf-8'))['data']['current_value']

    z = u'°C'


    str = 'Temp: ' + nt + z + '\n' + 'Set Temp:' + st + z

    return str


# def pic():
#    with picamera.PiCamera() as camera:
#        camera.resolution = (800, 600)
#        camera.start_preview()
#        time.sleep(1)
#        camera.capture('test.jpg')

# def pic():
#   rsp = requests.get(url2)
#    cont = rsp.content
#    buf = numpy.asarray(bytearray(cont), dtype="uint8")  # 转换为numpy数组
#    img = cv2.imdecode(buf, cv2.IMREAD_COLOR)  # 解码成图片
#    cv2.imwrite("D://1.jpg", img)  # 头像


itchat.auto_login(hotReload=True)


@itchat.msg_register(itchat.content.TEXT)
def text_reply(msg):
    messa = msg.text
    if messa == 'get':
        str = num()
        asker = msg['FromUserName']
        # pic()
        itchat.send(str, asker)
        itchat.send(str, toUserName='filehelper')
        return

    elif messa.startswith('t'):
        asker = msg['FromUserName']
        ser2.write(messa.encode())
        #ser2.close()
        itchat.send('set Temp :' + messa.lstrip('t') + '\n' + 'Warming-up', asker)
        itchat.send('set Temp :' + messa.lstrip('t') + '\n' + 'Warming-up', toUserName='filehelper')
        print(messa);

itchat.run()
