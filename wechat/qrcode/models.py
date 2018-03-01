#coding=utf8

from django.db import models

class RequestMessage(models.Model):
    msg_id   = models.IntegerField()              # 消息ID
    msg_type = models.CharField(max_length=32)    # 消息类型
    msg_src  = models.CharField(max_length=64)    # 消息来源
    msg_data = models.CharField(max_length=1024)  # 消息内容   
    msg_url  = models.CharField(max_length=128)   # 消息资源-URL

    
class ResponseMessage(models.Model):
    msg_id   = models.IntegerField()              # 消息ID
    msg_type = models.CharField(max_length=32)    # 消息类型
    msg_dst  = models.CharField(max_length=64)    # 目的用户
    msg_data = models.CharField(max_length=1024)  # 消息内容   
    msg_url  = models.CharField(max_length=128)   # 消息资源-URL


