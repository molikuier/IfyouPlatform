"""IfYouQualityPlatform URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from index import views

urlpatterns = [
    path('admin/', admin.site.urls,),
    path('test/', views.test_html),
    path('test_if/', views.test_if),
    path('hello_myweb/<int:id>', views.Hello_MyWeb, name="myweb"),
    path('test_for/', views.test_for),
    path('test_sort/', views.test_sort),
    path('test_url/', views.test_url),
    path('simple_tag/', views.simple_tag),
    path('inclu_tag/', views.inclu_tag),
    path('sim_tag/', views.sim_tag),
    path('if_change/', views.ifchanged),
]
