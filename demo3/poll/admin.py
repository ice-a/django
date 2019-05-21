from django.contrib import admin
from .models import test,Myuser
# Register your models here.
class testAdmin(admin.ModelAdmin):
    list_display = ['title', 'choseA', 'choseB', 'resualtA','resualtB']
    list_filter = ['title', 'choseA', 'choseB']
    list_per_page = 10
    search_fields = ['title', 'choseA', 'choseB']
admin.site.register(test,testAdmin)
admin.site.register(Myuser)
