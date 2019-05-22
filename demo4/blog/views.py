from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse
from .models import Article
from django.core.paginator import Paginator
import markdown
# Create your views here.

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
    return render(request,'single.html', locals())