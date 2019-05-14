from django.contrib import admin
from .models import book,hero
#一个功能强大的后台管理功能
# Register your models here.
admin.site.register(book)
admin.site.register(hero)

