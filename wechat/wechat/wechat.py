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

#text 修饰的 Handler 只处理文本消息
@wechat.text
def echo(message):
    print "Recive Text:" + message.img
    return message.content

#image 修饰的 Handler 只处理图片消息
@wechat.image
def image(message):
    print "Recive Image:" + message.img
    return message

#voice 修饰的 Handler 只处理语音消息
@wechat.voice
def voice(message):
    print "Recive Voice:" + message.recognition
    return message.recognition
    
#location 修饰的 Handler 只处理语音消息
@wechat.location
def location(message):
    return 'Hello My Friend!Location' + message.label
    
#subscribe 被关注 (Event)
@wechat.subscribe
def subscribe(message):
    return 'Hello My Friend!'

#location_event 修饰的 Handler 只处理上报位置 (Event)
@wechat.location_event
def location_event(message):
    return 'Location Success'

#click 修饰的 Handler 只处理自定义菜单事件 (Event)
@robot.click
def click(message):
    if message.key == "Warning":
        return "Uploading picture."
    if message.key == "Weather":
        return "Waiting for today's weather."




