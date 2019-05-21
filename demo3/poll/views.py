from django.shortcuts import render,redirect,reverse
from django.http import HttpResponse,HttpResponseRedirect
from django.template import loader
from django.contrib.auth import authenticate,login as lgi,logout as lgo
from .util import checklogin
from django.views.generic import View
from  .models import test,Myuser


def login(request):
    if request.method=="GET":
        return render(request,'poll/login.html')
    else:
        #使用django授权系统
        username=request.POST.get("username_login")
        pwd=request.POST.get("password_login")
        user = authenticate(request, username = username , password = pwd )
        if user:
            print(user)
            lgi(request, user)
            return redirect(reverse("poll:index"),{"user",user})
            # return render(request, 'poll/index.html', {"user": user})
        else:
            return render(request, 'poll/login.html', {"error": "用户名或者密码错误"})
def logout(request):
    res=redirect(reverse('poll:login'))
    lgo(request)
    return res
def register(request):
    if request.method=="POST":
        username=request.POST.get("username_register")
        pwd=request.POST.get("password_register")
        Myuser.objects.create_user(username=username,password=pwd,url='http://www.baidu.com')
        return redirect(reverse('poll:login'))
@checklogin
def index(request):
    tests = test.objects.all()
    tests = test.objects.all()
    temp = loader.get_template('poll/index.html')
    result = temp.render({"alltest": tests})
    return HttpResponse(result)
    # return render(request,'poll/index.html',locals())
@checklogin
def deatil(request,id):
    testtitle = test.objects.get(pk=id)
    if request.method=="POST":
        obj=test.objects.get(pk=id)
        if request.POST['sex']==obj.choseA:
            obj.resualtA=int(obj.resualtA)+1
            obj.save()
        elif request.POST['sex']==obj.choseB:
            obj.resualtB=int(obj.resualtB)+1
            obj.save()
        return HttpResponseRedirect("/poll/result/%s/"%id)
    return render(request, 'poll/deatil.html', {"testtitle": testtitle})
@checklogin
def result(request,id):
    obj = test.objects.get(pk=id)
    return render(request, 'poll/result.html', locals())
@checklogin
def addtest(request):
    if request.method=="GET":
        return render(request,'poll/addtest.html')
    elif request.method=="POST":
        newtest=test()
        newtest.title=request.POST["title"]
        newtest.choseA=request.POST["choseA"]
        newtest.choseB=request.POST["choseB"]
        newtest.save()
        return HttpResponseRedirect("/poll/index/")
@checklogin
def delete(request,id):
    obj=test.objects.get(pk=id)
    obj.delete()
    return HttpResponseRedirect("/poll/index/")
