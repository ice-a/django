from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.template import loader
from .models import brand,subbrand
# Create your views here.

def index(request):
    temp=loader.get_template('mall/index.html')
    result=temp.render({})
    return HttpResponse(result)

def list(request):
    allbrand=brand.objects.all()
    temp = loader.get_template('mall/list.html')
    result = temp.render({"allbrand":allbrand})
    return HttpResponse(result)

def deatil(request,id):
    brands=None
    try:
        brands=brand.objects.get(pk=id)
    except Exception as e:
        return HttpResponse("没有品牌信息")
    temp = loader.get_template('mall/deatil.html')
    result = temp.render({"brands":brands})
    return HttpResponse(result)
