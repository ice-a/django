from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from django.template import loader
from  .models import test
# Create your views here.
def index(request):
    tests = test.objects.all()
    temp = loader.get_template('poll/index.html')
    result = temp.render({"alltest": tests})
    return HttpResponse(result)
def deatil(request,id):
    testtitle=test.objects.get(pk=id)
    temp = loader.get_template('poll/deatil.html')
    result = temp.render({"testtitle": testtitle})
    return HttpResponse(result)
def result(request,id):
    print(id)
    return HttpResponse("测试联通，这里是的result")
