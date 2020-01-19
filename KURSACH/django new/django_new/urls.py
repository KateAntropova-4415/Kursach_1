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
    path('example', views.example, name='example'),
    path('', views.home, name='home'),
    #path('page2', views.points, name='page2'),
    path('trains', views.trains, name='trains'),
    path('login/', views.login, name='login'),
    path('account/', views.account, name='account'),
    path('administ/', views.administ, name='administ'),
    path('moder/', views.moder, name='moder'),
    url('(?P<station_id>\d+)', views.point_trains, name='station_detail_url'),
    url('(?P<point_name>\d+)', views.point_dep, name='trains_dep'),
    url('(?P<point_name>\d+)', views.point_arr, name='trains_arr'),
    #url('point_dep', views.point_dep, name='trains_dep'),
    #url('point_arr', views.point_arr, name='trains_arr'),
    path('departure/', views.departure, name='departure'),
    path('arrival/', views.arrival, name='arrival'),
    path('adduser/', views.adduser, name='adduser'),
    path('addstation/', views.addstation, name='addstation')
    
]
