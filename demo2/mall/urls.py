from django.conf.urls import url
from . import views
urlpatterns = [
    url('^list/$',views.list),
    url(r'^deatil/(\d+)/$',views.deatil),
    url(r'^index/$',views.index)
]
