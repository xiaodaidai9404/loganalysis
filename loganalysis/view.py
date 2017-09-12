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
def index(request):
    return render(request,'homepage/index.html')


@csrf_exempt
def country_loganalysis(request):
    return render(request,'homepage/country_ays.html')

@csrf_exempt
def country_get(request):
    post_data = request.POST
    date = post_data.get('search_date')
    key_list = redis_action.search_key(date)
    print (key_list)
    country_list = map(lambda x:bytes.decode(x).split('_')[1], key_list)
    print (country_list)
    value_list = redis_action.mget_redis(key_list)
    country_dict = dict(map(lambda x, y: [x, bytes.decode(y).split('_')[0]], country_list,value_list))
    print (country_dict)
    return HttpResponse(json.dumps({"code": 200, "result": country_dict}))