from django.conf.urls import url
from . import views
app_name="booktest"
urlpatterns = [
    url(r'^list/$',views.list,name="list"),
    url(r'^deatil/(\d+)/$',views.deatil,name="deatil"),
    url(r'^index/$',views.index,name='index'),
    url(r'^deletebook/(\d+)/$',views.deletebook,name='deletebook'),
    url(r'^deletehero/(\d+)/$',views.deletehero,name='deletehero'),
    url(r'^addhero/(\d+)/$',views.addhero,name='addhero'),
    url(r'^addbook/$',views.addbook,name='addbook'),
    url(r'^heroupdate/(\d+)/$',views.heroupdate,name='heroupdate'),
    url(r'^bookupdate/(\d+)/$',views.bookupdate,name='bookupdate'),
]
