from django.shortcuts import render,redirect,reverse
from django.http import HttpResponse,HttpResponseRedirect
from django.template import loader
from django.views.generic import View
from  .models import test,user
# Create your views here.
class Login(View):
    def get(self,request):
        return render(request,'poll/login.html')
    def post(self,request):
        username=request.POST.get("username")
        if username=='zzy':
            res=redirect(reverse('poll:index'))
            res.set_cookie('username',username)
            return  res
        else:
            return render(request, 'poll/login.html',{"error":"用户名或密码错误"})
def index(request):
    tests = test.objects.all()
    temp = loader.get_template('poll/index.html')
    result = temp.render({"alltest": tests})
    return HttpResponse(result)
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
def addtest(request):
    if request.method=="GET":
        return render(request,'poll/addtest.html')
    elif request.method=="POST":
        newtest=test()
        newtest.title=request.POST["title"]
        newtest.choseA=request.POST["choseA"]
        newtest.choseB=request.POST["choseB"]
        # newtest.resualtA=request.POST["resualtA"]
        # newtest.resualtB=request.POST["resualtB"]
        newtest.save()
        return HttpResponseRedirect("/poll/index/")
def delete(request,id):
    obj=test.objects.get(pk=id)
    obj.delete()
    return HttpResponseRedirect("/poll/index/")
