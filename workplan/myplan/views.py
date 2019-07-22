from django.http import JsonResponse, HttpResponse
from django.shortcuts import render

# Create your views here.
from myplan import models
from myplan.models import Plan, QA


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
    if request.method == 'GET':
        try:
            # qaName1 = QA(qaName=request.GET.get('qaName'))
            # qaName = models.QA.objects.filter(qaName=qaName1)
            obj = models.Plan.objects.filter(qaName='wanghc')
            print(obj)
            response = {"body":obj,"abc":"badsas "}
            # response['body'] = obj
            # response['msg'] = 'ok'
            # response['code'] = 0
            print(response)
        except  Exception as e:
            # response['msg'] = str(e)
            # response['error_num'] = 1
            pass
        # return JsonResponse(response)
        return HttpResponse(response)

