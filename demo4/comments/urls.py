from django.conf.urls import url,include
from . import views
from django.conf.urls import url
from .views import AddComment
app_name='comments'
urlpatterns = [
    url(r'^addcomment/(\d+)/$',view=AddComment.as_view(),name='addcomment')
]
