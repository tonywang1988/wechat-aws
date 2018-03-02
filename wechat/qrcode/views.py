# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse

from qrcode import models as qrcode_models
import json

# Create your views here.
 
def pullmessage(request):

    print 'Try to pull message...'

    # 获取全部待转发的用户消息
    messages = qrcode_models.RequestMessage.objects.all()

    msgarray = []
    for item in messages :
       dictitem = {}
       dictitem['msg_id']   = item.msg_id
       dictitem['msg_type'] = item.msg_type
       dictitem['msg_src']  = item.msg_src
       dictitem['msg_data'] = item.msg_data
       dictitem['msg_url']  = item.msg_url

       msgarray.append(dictitem)

    # 序列化json字符串
    jsonresp = json.dumps(msgarray,ensure_ascii=False)       

    # 删除相关消息记录
    messages.delete()

    print 'Take Message:' + jsonresp
     
    response =  HttpResponse(jsonresp)
    response.charset = 'UTF-8'
    response.content_type = 'application/json;charset=utf-8'
    
    return response

def pushmessage(request):

    message = json.loads(request.raw_post_data)

    print 'Try to push message : ' + request.raw_post_data

    # 获取全部待转发的用户消息
    message = qrcode_models.RequestMessage.objects.create(
        msg_id   = message['msg_id'],
        msg_type = message['msg_type'],
        msg_dst  = message['msg_dst'],
        msg_data = message['msg_data'],
        msg_url  = message['msg_url'])

    print 'Push Message' + message + ' To ' + message['msg_dst']
    
    return HttpResponse('Success')
