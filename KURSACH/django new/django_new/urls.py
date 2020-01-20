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
    #path('hello', views.indexRender, name='indexRender'),
    #path('ITMO', views.ITMO_University, name='ITMO'),
    #path('discipline', views.disc, name='discipline'),
    #path('group', views.group, name='group'),
    #path('departaments', views.deps, name='departaments'),
    #path('structureITMO', views.ITMO_structure, name='ITMOstructure'),
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
    path('addstation/', views.addstation, name='addstation'),
    path('addmoder/', views.addmoderator, name='addmoderator'),
    path('adduser/', views.adduser, name='addusers'),
    path('userlist/', views.userlist, name='userlist'),
    path('moderlist/', views.moderatorlist, name='moderatorlist'),
    path('stationlist/', views.stationlist, name='stationlist'),
    path('logout/', views.logout, name="logout"),
    #url(r'^town/(?P<station_id>\w{1,30})/$', views.point_trains_admin, name='station_detail_url_admin'),
    url(r'^stationlist/add-dep/(?P<station_id>\w{1,30})/$', views.addtripdep, name='addtripdep'),
    url(r'^stationlist/add-arr/(?P<id>\w{1,30})/$', views.addtriparr, name='addtriparr')
    
]
