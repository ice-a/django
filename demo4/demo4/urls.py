"""demo4 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/0002.0002/topics/http/urls/
Examples:
Function views
    0001. Add an import:  from my_app import views
    0002. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    0001. Add an import:  from other_app.views import Home
    0002. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    0001. Import the include() function: from django.urls import include, path
    0002. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf.urls import url,include
urlpatterns = [
    path('admin/', admin.site.urls),

    url('comments/',include('comments.urls',namespace='comments')),
    url('',include('blog.urls',namespace='blog')),
]
