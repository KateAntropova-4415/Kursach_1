"""
Definition of urls for django_new.
"""

#from datetime import datetime
from django.urls import path
from django.conf.urls import url
from django.contrib import admin
#from django.contrib.auth.views import LoginView, LogoutView
#from app import forms, views
from django_new import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('hello', views.indexRender, name='indexRender'),
    path('ITMO', views.ITMO_University, name='ITMO'),
    path('discipline', views.disc, name='discipline'),
    path('group', views.group, name='group'),
    path('departaments', views.deps, name='departaments'),
    path('structureITMO', views.ITMO_structure, name='ITMOstructure'),
    path('page1', views.page1, name='page1'),
    path('input', views.input, name='input'),
    path('example', views.example, name='example'),
    path('', views.home, name='home'),
    path('page2', views.page2, name='page2'),
    path('trains', views.trains, name='trains'),
    path('homes', views.homes, name='homes'),
    path('login/', views.login, name='login'),
    path('account/', views.account, name='account'),
    path('administ/', views.administ, name='administ'),
    path('moder/', views.moder, name='moder')
    
]
