from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from django.template import loader
from .models import book,hero
#MVT中的V，便于用户查看
# Create your views here.

def index(request):
    temp=loader.get_template('booktest/index.html')
    result=temp.render({"aaa":"hehe"})
    return HttpResponse(result)

def list(request):
    allbook=book.objects.all()
    temp = loader.get_template('booktest/list.html')
    result = temp.render({"allbook":allbook})
    return HttpResponse(result)

def deatil(request,id):
    books=None
    try:
        books=book.objects.get(pk=id)
    except Exception as e:
        return HttpResponse("没有书籍信息")
    temp = loader.get_template('booktest/deatil.html')
    result = temp.render({"books":books})
    return HttpResponse(result)
def deletebook(request,id):
    # return HttpResponse("success")
    book.objects.get(pk=id).delete()
    return HttpResponseRedirect('/booktest/list/')
def deletehero(request,id):
    heros=hero.objects.get(pk=id)
    bookid=heros.wj.id
    heros.delete()
    # return HttpResponse("success")
    return HttpResponseRedirect('/booktest/deatil/%s'%bookid)
def addhero(request,id):
    if request.method=="GET":
        return render(request,'booktest/addhero.html',{"bookid":id})
    elif request.method=="POST":
        chosebook=book.objects.get(pk =id)
        newhero=hero()
        newhero.name=request.POST["heroname"]
        newhero.gender=request.POST['sex']
        newhero.skill=request.POST['skill']
        newhero.wj=chosebook
        newhero.save()
        return HttpResponseRedirect("/booktest/deatil/%s/"%id)
def addbook(request):
    if request.method=="GET":
        return render(request,'booktest/addbook.html')
    elif request.method=="POST":
        newbook=book()
        newbook.title=request.POST["bookname"]
        newbook.pub_date=request.POST["pub_date"]
        newbook.save()
        return HttpResponseRedirect("/booktest/list/")
def heroupdate(request,id):
    if request.method=="GET":
        return render(request,'booktest/heroupdate.html',{"heroid":id})
    elif request.method=="POST":
        print("post")
        newhero=hero.objects.get(pk=id)
        bookid=newhero.wj.id
        newhero.name = request.POST["heroname"]
        newhero.gender = request.POST['sex']
        newhero.skill = request.POST['skill']
        newhero.save()
        return HttpResponseRedirect("/booktest/deatil/%s/"%bookid)
def bookupdate(request,id):
    if request.method=="GET":
        return render(request,'booktest/bookupdate.html',{"bookid":id})
    elif request.method=="POST":
        newbook=book.objects.get(pk=id)
        newbook.title=request.POST["bookname"]
        newbook.pub_date=request.POST["pub_date"]
        newbook.save()
        return HttpResponseRedirect("/booktest/list/")




