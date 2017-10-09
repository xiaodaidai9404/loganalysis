#!/usr/bin/python
#coding=utf-8
from django.http import HttpResponse
import sys
import json
import datetime

from django.http import JsonResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, Http404
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required
import loganalysis.redis_action as redis_action

@csrf_exempt
def alert_user(request):
    result = redis_action.get_alert_user()
    print (result)
    return render(request,"homepage/alert_user.html",{"result":result})

def add_alert_user(request):
    post_data = request.POST
    name = post_data.get('name')
    wechat = post_data.get('wechat')
    telephone = post_data.get('telephone')
    dingtalk = post_data.get('dingtalk')
    email = post_data.get('email')
    key = "alert_user_"+str(name)
    redis_action.hset_redis(key,name=name,wechat=wechat,telephone=telephone,email=email,dingtalk=dingtalk)
    if redis_action.exists_key(key):
        result = json.dumps({"code": 200, "msg": "添加成功"})
    else:
        result = json.dumps({"code": 500, "msg": "添加失败"})
    return HttpResponse({"result":result})

def del_alert_user(request):
    post_data = request.POST
    name = post_data.get('name')
    key = "alert_user_" + str(name)
    redis_action.del_key(key)
    if redis_action.exists_key(key):
        result = json.dumps({"code": 500, "msg": "删除失败"})
    else:
        result = json.dumps({"code": 200, "msg": "删除成功"})
    return HttpResponse({"result":result})

@csrf_exempt
def alert_rule(request):
    return render(request, "homepage/alert_rule.html")

def add_alert_rule(request):
    post_data = request.POST
    print (post_data)
    alert_type = post_data.get('alert_type')
    alert_type_value = post_data.get('alert_type_value')
    alert_type_rule = post_data.get('alert_type_rule')
    alert_value = post_data.get('alert_value')
    alert_user = post_data.get('alert_user')
    print ("alert_type "+alert_type)
    print ("alert_type_value "+alert_type_value)
    print ("alert_type_rule "+alert_type_rule)
    print ("alert_value "+alert_value)
    print ("alert_user "+alert_user)
    key = str(alert_type)+"_"+str(alert_type_value)+"_"+str(alert_type_rule)
    print (key)
    return HttpResponse({"result": json.dumps({"code": 200, "msg": "测试"})})