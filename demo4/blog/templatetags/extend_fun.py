from django import template
from ..models import Article,Category,Tag,Abs
register = template.Library()

@register.filter(name='mylower')
def mylower(value):
    return value.lower()

@register.filter(name='myslice')
def myslice(value,length):
    result = value[:length]
    print(result)
    return  result

@register.simple_tag(name='getcategorys')
def getcategorys():
    return Category.objects.all()

@register.simple_tag
def getlatestarticles(num=3):
    return Article.objects.all().order_by('-create_time')[:num]

@register.simple_tag
def getarchives(num=3):
    return Article.objects.dates("create_time",'month',order='DESC')[:num]

@register.simple_tag
def gettags():
    return Tag.objects.all()

@register.simple_tag
def getabs():
    return Abs.objects.all()