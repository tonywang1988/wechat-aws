#coding=utf8
from werobot import WeRoBot

wechat = WeRoBot(enable_session=False,
                token='awswechat',
                APP_ID='wxf02b4fc833408f5b',
                APP_SECRET='682f69ee4068420fb11c74aaf3059b12')

client = wechat.client
client.create_menu({
    "button":[
        {
            "type":"click",
            "name":"Warning",
            "key":"V1001_TODAY_WARNING"
        },
        {
            "type":"click",
            "name":"Weather",
            "key":"V1001_TODAY_WEATHER"
        },
        {
            "name":"Help",
            "sub_button":[
                {
                    "type":"view",
                    "name":"Home",
                    "url":"http://www.shipxy.com"
                },
                {
                    "type":"view",
                    "name":"Service",
                    "url":"http://www.cetc.com.cn"
                }
            ]
       }]
})

 
@wechat.handler
def hello(message):
  return message.content 

#text 修饰的 Handler 只处理文本消息
@wechat.text
def echo(message):
    return message.content

#image 修饰的 Handler 只处理图片消息
@wechat.image
def image(message):
    print message.img
    return message.img

#subscribe 被关注 (Event)
@wechat.subscribe
def subscribe(message):
    return 'Hello My Friend!'

#voice 修饰的 Handler 只处理语音消息
@wechat.voice
def voice(message):
    return 'Hello My Friend!'

#location_event 修饰的 Handler 只处理上报位置 (Event)
@wechat.location_event
def location(message):
    return 'Location Success'

@robot.click
def abort(message):
    if message.key == "Please upload picture.WarningWarningWarningWarningWarningWarning":
        return "I'm a robot"


wsddefef


