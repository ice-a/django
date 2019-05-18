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
# def deatil(request,id):
#     if request=="POST":
#         return HttpResponse("测试已经联通，返回了post")
#     elif request=="GET":
#         return HttpResponse("测试已经联通，返回了get")
#     else:
#         print("get")
#         return HttpResponse("测试已经联通，返回了else")
        # testtitle = test.objects.get(pk=id)
        # temp = loader.get_template('poll/deatil.html')
        # result = temp.render({"testtitle": testtitle})
        # return HttpResponse(result)
        # return render(request, 'poll/deatil.html', {"testtitle": testtitle})
#
def deatil(request,id):
    if request.method=="GET":
        testtitle = test.objects.get(pk=id)
        # temp = loader.get_template('poll/deatil.html')
        # result = temp.render({"testtitle": testtitle})
        # return HttpResponse(result)
        return render(request, 'poll/deatil.html', {"testtitle": testtitle})
    elif request.method=="POST":
        obj=test.objects.get(pk=id)
        print(obj.resualtA)
        print(obj.resualtB)
        print(test)
        if request.POST['sex']==obj.choseA:
            obj.resualtA=int(obj.resualtA)+1
            obj.save()
        elif request.POST['sex']==obj.choseB:
            obj.resualtB=int(obj.resualtB)+1
            obj.save()
        print(obj.resualtA)
        print(obj.resualtB)
        return HttpResponseRedirect("/poll/result/%s/"%id)
    else:
        return HttpResponse("不识别get和post")
def result(request,id):
    obj = test.objects.get(pk=id)
    return render(request, 'poll/result.html', {"obj": obj})
