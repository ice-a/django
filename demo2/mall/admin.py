from django.contrib import admin
from .models import brand,subbrand
# Register your models here.
class subbrandInine(admin.StackedInline):
    model = subbrand
    extra = 1
class brandAdmin(admin.ModelAdmin):
    list_display = ["brandname",'pub_data']
    list_filter = ["brandname",'pub_data']
    list_per_page = 5
    search_fields = ["brandname",'pub_data']
    inlines = [subbrandInine]
class subbrandAdmin(admin.ModelAdmin):
    list_display = ['subbrandname','color','memory']
    list_filter = ['subbrandname','color','memory']
    list_per_page = 5
    search_fields = ['subbrandname','color','memory']
admin.site.register(brand,brandAdmin)
admin.site.register(subbrand,subbrandAdmin)

