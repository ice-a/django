from django.conf.urls import url
from . import views
app_name="poll"
urlpatterns = [
    url(r'^result/(\d+)/$',views.result,name='result'),
    url(r'^deatil/(\d+)/$',views.deatil,name='deatil'),
    url(r'^index/$',views.index,name='index'),
    url(r'^addtest/$',views.addtest,name='addtest'),
    url(r'^delete/(\d+)/$',views.delete,name='delete'),
]
