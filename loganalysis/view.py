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

def test(request):
    return render(request,'test.html')

@csrf_exempt
def country_loganalysis(request):
    return render(request,'homepage/country_ays.html')

@csrf_exempt
def country_get(request):
    post_data = request.POST
    date1 = post_data.get('search_date')
    result = redis_action.yester_contrast(date1)
    return HttpResponse(json.dumps({"code": 200, "result": result}))

@csrf_exempt
def http_code_loganalysis(request):
    return render(request,'homepage/http_code_ays.html')

@csrf_exempt
def http_code_get(request):
    post_data = request.POST
    date1 = post_data.get('search_date')
    result = redis_action.yester_http_code(date1)
    return HttpResponse(json.dumps({"code": 200, "result": result}))

@csrf_exempt
def slow_url_loganalysis(request):
    return render(request,'homepage/nginx_slow_url_ays.html')

@csrf_exempt
def     slow_url_domain(request):
    post_data = request.POST
    date1 =  post_data.get('search_date')
    result = redis_action.get_domain(date1)
    print (result)
    return HttpResponse(json.dumps({"code":200,"result": result}))

@csrf_exempt
def slow_url_get(request):
    post_data = request.POST
    date1 = post_data.get('search_date')
    domain = post_data.get('domain')
    key = date1+"_http_domain_"+domain+"_slow_url"
    print (key)
    result = redis_action.get_domain_slow_url(key)
    print (result)
    return HttpResponse(json.dumps({"code": 200, "result": result}))

def echarts_make(request):
    weekday_day = redis_action.get_day_7_list()
    country = redis_action.get_country_list()
    country_data_list = redis_action.get_country_data()
    country_list = []
    for num in range(0,5):
        country_list.append(country_data_list[num]['country'])

    for num in range(0, 5):
        del country_data_list[num]['country']

    country_access_list = []

    for num in range(0,5):
        country_access_tmp_list = []
        for item in sorted(country_data_list[num].keys(), reverse=True):
            country_access_tmp_list.append(country_data_list[num][item])
        country_access_list.append(country_access_tmp_list)

    return render(request,"homepage/echarts.html",{"weekday_day":weekday_day,"country":country,
                                                   "country1":country_list[0],"country2":country_list[1],"country3":country_list[2],"country4":country_list[3],"country5":country_list[4],
                                                   "country1_access_list":country_access_list[0],"country2_access_list":country_access_list[1],"country3_access_list":country_access_list[2],"country4_access_list":country_access_list[3],"country5_access_list":country_access_list[4]})