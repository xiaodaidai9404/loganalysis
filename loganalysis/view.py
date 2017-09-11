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
import es_action


reload(sys)

sys.setdefaultencoding('utf8')

#@csrf_exempt
def hello(request):
    return HttpResponse('hello world')

def index(request):
    return render(request, 'homepage/index.html')

@csrf_exempt
def es_get(request):
    post_data = request.POST
    # print post_data
    index = post_data.get('index')
    ip = post_data.get('host')
    command = post_data.get('command')
    # print index,ip,command
    if index == "":
        return HttpResponse(json.dumps({"code": 400, "msg": "index not allow None"}))
    if ip == "" and command == "":
        return HttpResponse(json.dumps({"code": 400, "msg": "Two args are not allowed to be empty at the same time"}))
    elif ip and command == "":
        result = es_action.get(index, serverip=ip)
    elif command and ip == "":
        result = es_action.get(index, command=command)
    else:
        result = es_action.get(index,serverip=ip,command=command)
    print type(result),result
    return HttpResponse(json.dumps({"code": 200, "result": result}))
    # return JsonResponse(result,",safe=False)
    # return render(request,'homepage/index.html',{"result": result})
