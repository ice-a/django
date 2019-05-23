from django.shortcuts import render,get_object_or_404,redirect,reverse
from django.http import HttpResponse
from .models import Article,Category,Tag
from django.core.paginator import Paginator
import markdown
from django.views.generic import View
from .forms import ContactForm
from datetime import datetime
# Create your views here.
from comments.forms import CommentForm
def index(request):
    pagenum = request.GET.get("page")
    pagenum = 1 if pagenum==None  else pagenum
    articles = Article.objects.all().order_by("-views")
    paginator = Paginator(articles,1)
    page = paginator.get_page(pagenum)

    return render(request,'index.html',{"page":page})
def detail(request, id):
    article = get_object_or_404(Article, pk = id )
    mk = markdown.Markdown(extensions=[
        "markdown.extensions.extra",
        "markdown.extensions.codehilite",
        "markdown.extensions.toc"
    ] )
    article.body = mk.convert(article.body)
    article.toc = mk.toc
    cf=CommentForm()

    return render(request,'single.html', locals())
def archives(request,year,month):
    articles=Article.objects.filter(create_time__year=year,create_time__month=month)
    paginator = Paginator(articles, 1)
    page = paginator.get_page(1)
    return render(request,'index.html',{'page':page})
def category(request,id):

    pagenum = request.GET.get("page")
    pagenum = 1 if pagenum == None else pagenum

    articles = get_object_or_404(Category,pk=id).article_set.all()
    paginator = Paginator(articles, 1)
    # 传入页码得到一个页面   page包含所有信息
    page = paginator.get_page(pagenum)
    page.parms = "/category/%s/"%(id,)
    return render(request, 'index.html', {"page": page })

def tag(request,id):
    pagenum = request.GET.get("page")
    pagenum = 1 if pagenum == None else pagenum

    articles = get_object_or_404(Tag, pk=id).article_set.all()
    paginator = Paginator(articles, 1)
    # 传入页码得到一个页面   page包含所有信息
    page = paginator.get_page(pagenum)
    page.parms = "/tag/%s/"%(id,)
    return render(request, 'index.html', {"page": page})

class Contacts(View):
    def get(self,request):
        cf = ContactForm()
        return render(request, 'contact.html',locals())
    def post(self,request):
        cf = ContactForm(request.POST)
        cf.save()
        cf = ContactForm()
        return render(request, 'contact.html', {"info":'成功',"cf":cf})
