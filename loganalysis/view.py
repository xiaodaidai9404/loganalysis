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
    date = '2017-09-09'
    key_list = redis_action.search_key(date)
    country_list = map(lambda x:x.split('_')[1], key_list)
    value_list = redis_action.mget_redis(key_list)
    country_dict = dict(map(lambda x, y: [x, y], country_list,value_list))
    print (country_dict)
    return render(request, 'homepage/index.html')