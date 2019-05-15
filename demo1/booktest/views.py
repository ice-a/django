from django.shortcuts import render
from django.http import HttpResponse
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
