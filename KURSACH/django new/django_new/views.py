"""
Definition of views.
"""

from django.http import HttpResponse
from django.shortcuts import render
from app.forms import *
from django.http import HttpResponse
from django.shortcuts import redirect
from django.views.decorators.csrf import csrf_exempt

import json
#from .models import station


with open("json_data1.json", 'r') as read_file:
    data = json.load(read_file)
    stations = data['railway_station']
    
        

with open("json_data.json", 'r') as read_file:
    data = json.load(read_file)
    
    name = data['name']

    head_name = data['head']['name']
    head_surname = data['head']['surname']

    
    index = data['location']['index']
    city = data['location']['city']
    adress = data['location']['adress']

    
    ad_amount = len(data['administrative'])

    
    sc_amount = len(data['scintific_and_educational'])

    
    mf_amount = 0
    for i in data['scintific_and_educational']:
        if i['name'].find("Мегафакультет") != -1:
            mf_amount += 1

    meg_id= data['scintific_and_educational'][0]['id']

    meg_name=data['scintific_and_educational'][0]['name']

    megITMO = {'meg_id': meg_id,
               'meg_name':meg_name}

    dep_amount = 0
    for i in data['scintific_and_educational']:
        dep_amount += len(i['departments'])


    

    edp_id = data['scintific_and_educational'][0]['departments'][0]['educational_programs'][0]['id']

    
    edp_name = data['scintific_and_educational'][0]['departments'][0]['educational_programs'][0]['name']

    
    dis_name = data['scintific_and_educational'][0]['departments'][0]['educational_programs'][0]['discipline']

    
    year_of_study = data['scintific_and_educational'][0]['departments'][0]['educational_programs'][0]['year']

    
    administrative = data['administrative']

    
    amount_of_groups = len(year_of_study['groups'])

    
    group = year_of_study['groups'][0]

    
    deps = data['scintific_and_educational'][0]['departments']


    
    dict_ITMO = {'name': name, 'head': [head_name, head_surname],
            'adress': {'index': index, 'city': city, 'adress': adress},
            'ad_amount': ad_amount,
            'sc_amount': sc_amount,
            'mf_amount': mf_amount,
            'dep_amount': dep_amount}

    
    dict_disc = {
                 'edp_id': edp_id,
                 'edp_name': edp_name,
                 'dis_name': dis_name,
                 'year_of_study': year_of_study,
                 'amount_of_groups': amount_of_groups}

    
    dict_group = {'group': group}

    
    dict_deps = {'departaments': deps}

    
    dict_uni = {'administrative': administrative}
    dict_uni.update(megITMO)
 
    dict_uni.update(dict_deps)
    
    dict_uni.update(dict_ITMO)


def index(request):
    return HttpResponse("Hello, World!")
def indexRender(request):
    return render(request, 'index.html', {})
def ITMO_University(request):
    return render(request, 'universityInfo.html', dict_ITMO)
def disc(request):
    return render(request, 'disciplineInfo.html', dict_disc)
def group(request):
    return render(request, 'groupsInfo.html', dict_group)
def deps(request):
    return render(request, 'departamentsInfo.html', dict_deps)
def ITMO_structure(request):
    return render(request, 'universityStructure.html', dict_uni)
def page1(request):
    return render(request, 'Page1.html', {})
def input(request):
    return render(request, 'Input.html', {})
def example(request):
    return render(request, 'Example.html', {})
def home(request):
    return render(request, 'HomePage.html', {} )
def page2(request):
    return render(request, 'page2.html', {})
def trains(request):
    return render(request, 'trains.html', {})
def homes(request):
    return render(request, 'home.html', {})

def account(request):
    page = 'account.html'
    if "id" not in request.session:
        page = "error_404.html"
    return render(request, page, {})

def administ(request):
    page = 'admin.html'
    if "id" not in request.session:
        page = "error_404.html"
    return render(request, page, {})

def moder(request):
    page = 'moder.html'
    if "id" not in request.session:
        page = "error_404.html"
    return render(request, page, {})

def account(request):
    page = 'account.html'
    if "id" not in request.session:
        page = "error_404.html"
    return render(request, page, {})

def login(request):
    logForm = LoginForm(request.POST or None)
    error = 'None'
    if 'id' in request:
        return redirect("/account")
    if request.POST:
        with open("users.json", 'rb') as read_file_json:
            users = json.load(read_file_json)
        req = request.POST
        # Проверка входа в систему
        checkLogin = req.get("login")
        checkPass = req.get("password")
        error = 'Неправильно введён логин или пароль'
 #       checkFunc = "none"
        for user in users['users']:
            if user['login'] == checkLogin and user['password'] == checkPass:
                request.session.set_expiry(15)
                request.session['id'] = user['id']
                request.session['login'] = user['login']
                request.session['position'] = user['position']
                if request.session['position'] == "Admin":
                    return redirect("/administ")
                elif request.session['position'] == "Moder":
                    return redirect("/moder")
                elif request.session['position'] == "User":
                    return redirect("/account")
                # return redirect("/account")

    return render(request, 'login.html', {'form': logForm,
                                          'error': error}) 
