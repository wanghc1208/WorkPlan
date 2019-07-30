
from django.contrib import auth
from django.http import JsonResponse, HttpResponse
from django.shortcuts import render
import json
from django.core import serializers
from django.core.serializers.json import DjangoJSONEncoder


# Create your views here.
from myplan import models
from myplan.models import Plan, User


def Login(request):
    try:
        user = request.POST.get('username',None)
        pwd = request.POST.get('password',None)
        queryset = User.objects.get(name=user)
        obj = auth.authenticate(request, username=user, password=pwd)
        if user==queryset.name&pwd==queryset.password:
            return JsonResponse({'code':'0','message':'账号密码验证成功'})
    except:
        return JsonResponse({'code':'1','message':'验证失败'})


def add_plan(request):
    response = {}
    if request.method == 'POST':
        try:
            reqdata=json.loads(request.body)
            print(reqdata,"woshishui")
            name=reqdata["name"]
            group=reqdata["group"]
            arraylist = reqdata["planList"]
            # name = request.POST.get('name'),
            # array = request.POST.getlist('planList')
            print(name,"12131")
            print(arraylist,"1231321")
            uname = models.User.objects.get(name=name)
            for i in arraylist:
                planTime = i["planTime"]
                print(planTime,"time！！！！！！")
                moringPlanName =i["moringPlanName"]
                afternoonPlanName = i["afternoonPlanName"]
                planName = moringPlanName+'@@'+afternoonPlanName
                print(planName)
                Plan.objects.filter(uname=uname, planTime=planTime).delete()
                models.Plan.objects.create(uname=uname, planTime=planTime, PlanName=planName).save()
            response['msg'] = 'ok'
            response['code'] = 0
        except  uname.DoesNotExist:
            models.User.objects.create(name=name, group=group)
            uname = models.User.objects.get(name=name)
            models.Plan.objects.create(uname=uname, planTime=planTime, PlanName=planName).save()
            response['msg'] = 'ok'
            response['code'] = 0
        return JsonResponse(response)
    else:
        return HttpResponse("hello  你好!a")


def show_plan(request):
    response ={}
    response1 = {}
    if request.method == 'GET':
        try:
            user = models.User.objects.filter(name='wanghc')
            objs = models.Plan.objects.filter(planTime__gte='2019-07-26',planTime__lte='2019-07-31').order_by('-planTime')
            plan = json.loads(serializers.serialize("json", objs))
            response['user'] = json.loads(serializers.serialize("json", user))
            response['plan'] = json.loads(serializers.serialize("json", objs))
            print(response)
            response['success'] = 'true'
            response['code'] = 0
        except  Exception as e:
            response['msg'] = str(e)
            response['error_num'] = 1
            # pass
        return JsonResponse(response,charset='utf-8',safe=False)

        # return HttpResponse(response1)

