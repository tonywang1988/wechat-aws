#coding=utf8
from werobot import WeRoBot
from urllib import urlretrieve
from werobot.replies import ImageReply
from qrcode import models as qrcode_models
import json
import logging

logging.basicConfig()

wechat = WeRoBot(enable_session=False,
                token='awswechat',
                APP_ID='wxf02b4fc833408f5b',
                APP_SECRET='682f69ee4068420fb11c74aaf3059b12')

client = wechat.client
##client.create_menu({
##    "button":[
##        {
##            "type":"click",
##            "name":"Warning",
##            "key":"V1001_TODAY_WARNING"
##        },
##        {
##            "type":"click",
##            "name":"Weather",
##            "key":"V1001_TODAY_WEATHER"
##        },
##        {
##            "name":"Help",
##            "sub_button":[
##                {
##                    "type":"view",
##                    "name":"Home",
##                    "url":"http://www.shipxy.com"
##                },
##                {
##                    "type":"view",
##                    "name":"Service",
##                    "url":"http://www.cetc.com.cn"
##                }
##            ]
##       }]
##})

# 通过修饰符添加handler
@wechat.handler
def echo(message):
    return 'Hello World!'

#text 修饰的 Handler 只处理文本消息
@wechat.text
def echo(message):
    print 'Recive Text:' + message.content

    #return message.content

    msg_obj = qrcode_models.RequestMessage.objects.create(
        msg_id   = message.message_id,
        msg_type = message.type,
        msg_src  = message.source,
        msg_data = message.content,
        msg_url  = '')
    msg_obj.save() 
    return 'Text['+message.content+'] Processing ...'

#image 修饰的 Handler 只处理图片消息
@wechat.image
def image(message):
    print 'Recive Image:' + message.img

    #下载文件并上传资源，重新返回
    #urlretrieve(message.img,'/home/ubuntu/wechat-aws/wechat/media_file.jpg') 
    #media_file = open('/home/ubuntu/wechat-aws/wechat/media_file.jpg')
    #print 'Download image as /home/ubuntu/wechat-aws/wechat/media_file for upload'   
    #media_resp = client.upload_media('image', media_file)
    #print 'Upload media id is '+media_resp['media_id'] 
    
    #应答格式{"type":"TYPE","media_id":"MEDIA_ID","created_at":123456789}
    #media_dict = json.loads(media_resp)
    #print 'Return media:'+media_dict
    #reply = ImageReply(message=message, media_id=media_resp['media_id'])
    #return reply 

    msg_obj = qrcode_models.RequestMessage.objects.create(
        msg_id   = message.message_id,
        msg_type = message.type,
        msg_src  = message.source,
        msg_data = message.img,
        msg_url  = message.img)
    msg_obj.save()
    return 'Image[' + message.img + '] Processing ...'

     
#voice 修饰的 Handler 只处理语音消息
@wechat.voice
def voice(message):
    print 'Recive Voice:' + message.media_id
    #return message.recognition

    msg_obj = qrcode_models.RequestMessage.objects.create(
        msg_id   = message.message_id,
        msg_type = message.type,
        msg_src  = message.source,
        msg_data = message.recognition,
        msg_url  = message.media_id)
    msg_obj.save()
    return 'Voice[' + message.recognition + '] Processing...'
    
#location 修饰的 Handler 只处理语音消息
@wechat.location
def location(message):
    print 'Recive Location:'
    return 'Hello My Friend!Location' + message.label
    
#subscribe 被关注 (Event)
@wechat.subscribe
def subscribe(message):
    return 'Hello My Friend!'

#location_event 修饰的 Handler 只处理上报位置 (Event)
@wechat.location_event
def location_event(message):
    print 'Recive Location Event:'
    return 'Location Success!' 

#click 修饰的 Handler 只处理自定义菜单事件 (Event)
@wechat.click
def click(message):
    print 'Recive Menu Event:' + message.key
    if message.key == "V1001_TODAY_WARNING":
        return "Please Uploading Picture..."
    if message.key == "V1001_TODAY_WEATHER":
        return "Waiting For Weather Report..."




