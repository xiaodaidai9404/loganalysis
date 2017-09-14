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