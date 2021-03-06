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
    path('', views.home, name='home'),
    path('login/', views.login, name='login'),
    path('account', views.account, name='account'),
    url('point/(?P<station_id>\d+)', views.point_trains, name='station_detail_url'),
    path('adduser/', views.adduser, name='adduser'),
    path('addstation/', views.addstation, name='addstation'),
    path('addmoder/', views.addmoderator, name='addmoderator'),
    path('adduser/', views.adduser, name='addusers'),
    path('addusernew/', views.addusernew, name='addusersnew'),
    path('userlist', views.userlist, name='userlist'),
    path('moderlist', views.moderatorlist, name='moderatorlist'),
    path('stationlist', views.stationlist, name='stationlist'),
    path('stationlistuser', views.stationlistuser, name='stationlistuser'),
    path('logout/', views.logout, name="logout"),
    url(r'^town/(?P<station_id>\w{1,30})/$', views.point_trains_admin, name='station_detail_url_admin'),
    url(r'^stationlist/add-dep/(?P<station_id>\w{1,30})/$', views.addtripdep, name='addtripdep'),
    url(r'^stationlist/add-arr/(?P<id>\w{1,30})/$', views.addtriparr, name='addtriparr'),
    url(r'$', views.error404, name='error404')
]
