from django.contrib import auth
from django.http import JsonResponse, HttpResponse
from django.shortcuts import render
import json
from django.core import serializers
from django.core.serializers.json import DjangoJSONEncoder


# Create your views here.
from myplan import models
from myplan.models import Plan, User, PlanDate


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
            # qaName=request.POST.get('qaName'),
            qaName = models.QA.objects.get(pk=1)
            planName = models.PlanType.objects.get(pk=2)
            planTime=request.POST.get('planTime')
            print(planTime)
            # planName=request.POST.get('planName')
            models.Plan.objects.create(qaName=qaName, planTime=planTime,planName=planName).save()

            response['msg'] = 'ok'
            response['code'] = 0
        except  Exception as e:
            response['msg'] = str(e)
            response['code'] = 1
        return JsonResponse(response)
    else:
        return HttpResponse("hello  你好!a")


def show_plan(request):
    response ={}
    response1 = {}
    if request.method == 'GET':
        try:
            objs = models.Plan.objects.all()
            objs1 = models.PlanDate.objects.all()
            response['list'] = json.loads(serializers.serialize("json", objs))
            response['list1'] = json.loads(serializers.serialize("json", objs1))
            # response['data2'] = serializers.serialize("json", PlanData.objects.filter(field="wanghc"))
            # queryset = PlanData.objects.filter(uname="wanghc").values('uname', 'planTime')
            # data = json.dumps(list(queryset), cls=DjangoJSONEncoder)
            # response['data'] = json.loads(serializers.serialize("json", data))
            # response['list2']= json.loads(serializers.serialize("json", PlanData.objects.all(), fields = ('uname', 'planTime')))
            response['msg'] = 'success'
            response['code'] = 0
            print(response)
        except  Exception as e:
            # response['msg'] = str(e)
            # response['error_num'] = 1
            pass
        return JsonResponse(response)
        # return HttpResponse(response1)

