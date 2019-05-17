from django.contrib import admin
from .models import book,hero,testmanage
#一个功能强大的后台管理功能
# Register your models here.
class heroInine(admin.StackedInline):
    model = hero
    extra = 1
class bookAdmin(admin.ModelAdmin):
    list_display = ["title",'pub_date']
    list_filter = ["title",'pub_date']
    list_per_page = 10
    search_fields = ["title",'pub_date']
    inlines = [heroInine]
class heroAdmin(admin.ModelAdmin):
    list_display = ['name','gender','skill','wj']
    list_filter = ['name','gender','skill','wj']
    list_per_page = 10
    search_fields = ['name','gender','skill','wj']
admin.site.register(book,bookAdmin)
admin.site.register(hero,heroAdmin)


