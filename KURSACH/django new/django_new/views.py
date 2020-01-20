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

Loginglobal = "none"
Passglobal = "none"
Funcglobal = "none"

with open("json_data1.json", encoding='utf-8') as read_file:
    data = json.load(read_file)
    stations = data['railway_station']
    dict_stations = {'railway_station': stations}

def example(request):
    return render(request, 'Example.html', {})
def home(request):
    with open("json_data1.json", encoding='utf-8') as read_file:
        data = json.load(read_file)
        stations = data['railway_station']
        dict_stations = {'railway_station': stations}
    return render(request, 'HomePage.html', dict_stations)
def page2(request):
    return render(request, 'page2.html', {})
def trains(request):
    return render(request, 'trains.html', {})

def account(request):
    page = 'account.html'
    if "id" not in request.session:
        page = "404.html"
    return render(request, page, {})

def administ(request):
    page = 'admin.html'
    if "id" not in request.session:
        page = "404.html"
    return render(request, page, {})

def moder(request):
    page = 'moder.html'
    if "id" not in request.session:
        page = "404.html"
    return render(request, page, {})

def account(request):
    page = 'account.html'
    if "id" not in request.session:
        page = "404.html"
    return render(request, page, {})

def login(request):
    logForm = LoginForm(request.POST or None)
    error = 'None'
    global Loginglobal
    global Passglobal
    global Funcglobal
    #if 'id' in request:
    #return redirect("/account")
    if request.POST:
        with open("users.json", 'rb') as read_file_json:
            users = json.load(read_file_json)
        req = request.POST
        # Проверка входа в систему
        checkLogin = req.get("login")
        checkPass = req.get("password")
        error = 'Неправильно введён логин или пароль'
        for user in users:
            if user['login'] == checkLogin and user['password'] == checkPass:
                checkFunc = user['position']
                Loginglobal = checkLogin
                Passglobal = checkPass
                Funcglobal = checkFunc
                request.session.set_expiry(8000)
                request.session['id'] = user['id']
                request.session['login'] = user['login']
                request.session['position'] = user['position']
                if request.session['position'] == "Admin":
                    return redirect("/administ")
                elif request.session['position'] == "Moder":
                    return redirect("/moder")
                elif request.session['position'] == "User":
                    return redirect("/account")

    return render(request, 'login.html', {'form': logForm,
                                          'error': error})

def point_trains(request, station_id):
    with open("json_data1.json", encoding='utf-8') as read_file:
        data = json.load(read_file)
        station_id = int(station_id)
        station_name = data['railway_station'][station_id]['name']
        station_adress = data['railway_station'][station_id]['address']
        trips_dep = data['railway_station'][station_id]['trips'][0]['departure']
        trips_arr = data['railway_station'][station_id]['trips'][0]['arrival']
        dict_trips = {  'name': station_name,
                        'address':station_adress,
                        'departure': trips_dep,
                        'arrival': trips_arr}

    return render(request, 'point-trains.html', dict_trips)

#def points(request):
#    with open("points.json", 'r') as read_file:
#        data = json.load(read_file)
#        point_dep=data['point'][0]['departure']
#        point_arr=data['point'][0]['arrival']
#        dict_point={ 'points_dep':point_dep,
#                     'points_arr':point_arr
#                    }
#    return render(request, 'page2.html', dict_point)

def point_dep(request, point_name):
    with open("json_data1.json", encoding='utf-8') as read_file:
        data = json.load(read_file)
        station=data['railway_station']
        dict_train_dep={}
        dict_train_ex={}
        for i in station:
            trip = i['trips'][0]['departure']
            for j in trip:
                if j['departure'] == point_name:
                    name_stat = i['name']
                    dep_point = j
                    #arr_point.append(name_stat)
                    dict_train_ex={ 'name' : name_stat,
                                   'points':dep_point
                        }
                    dict_train_dep.update(dict_train_ex)
                    dict_train_ex.clear() 

    return render(request, 'trains_dep.html', dict_train_dep)

def point_arr(request, point_name):
    with open("json_data1.json", encoding='utf-8') as read_file:
        data = json.load(read_file)
        station = data['railway_station']
        dict_train_arr = {}
        dict_train_ex = {}
        for i in station:
            for j in i['arrival']:
                if j['arrival'] == point_name:
                    name_stat  =i['name']
                    arr_point = j
                    arr_point.append(name_stat)
                    dict_train_ex= { 'name' : name_stat,
                                    'points':arr_point
                                   }
                    dict_train_arr.update(dict_train_ex)
                    dict_train_ex.clear() 

    return render(request, 'trains_arr.html', dict_train_arr)

def departure(request):
    with open("points.json", 'r') as read_file:
        data = json.load(read_file)
        point_dep=data['point'][0]['departure']
        dict_point={ 'points':point_dep
                    }
    return render(request, 'departure.html', dict_point)

def arrival(request):
    with open("points.json", 'r') as read_file:
        data = json.load(read_file)
        point_arr=data['point'][0]['arrival']
        dict_point1={ 
                     'points':point_arr
                    }
    
    return render(request, 'arrival.html', dict_point1)

def addstation(request):
    if request.POST:
        with open("json_data1.json", encoding='utf-8') as read_file_json:
            data = json.load(read_file_json)
        Station = data
        req = request.POST
        checkName = req.get("name")
        checkAddress = req.get("address")
        #checkTime = req.get("Time")
        checkerror = True
        trip=[{
            "departure":[],
            "arrival":[]
            }]
        
        for i in Station['railway_station']:
            if checkName == i['name']:
                print("Error")
                checkerror = False
                break
        if checkerror:
            ID = len(Station["railway_station"])
            newStation = {
                "id": ID,
                "name": checkName,
                "address": checkAddress,
                "trips": trip
            }
            data["railway_station"].append(newStation)
            with open('json_data1.json', 'w', encoding='utf-8') as read_file_json:
                read_file_json.write(json.dumps(data, ensure_ascii=False, separators=(',', ': '), indent=2))

    return render(request, "addstation.html", {})

@csrf_exempt
def adduser(request):
    if request.POST:
        userform = AddUser()
        with open("users.json", encoding='utf-8') as read_file_json:
            data = json.load(read_file_json)
        users = data
        req = request.POST
        checkLogin = req.get("login")
        checkPass = req.get("password")
        checkerror = True
        for i in users:
            if checkLogin == i['login']:
                print("Error")
                checkerror = False
                break
        if checkerror:
            ID = len(users) + 1
            newuser = {
                "login": checkLogin,
                "id": ID,
                "password": checkPass,
                "position": "User"
            }
            users.append(newuser)
            with open('users.json', 'w', encoding='utf-8') as read_file_json:
                read_file_json.write(json.dumps(users, ensure_ascii=False, separators=(',', ': '), indent=2))

    return render(request, "adduser.html", {})


@csrf_exempt
def addmoderator(request):
    if request.POST:
        userform = AddUser()
        with open("users.json", encoding='utf-8') as read_file_json:
            data = json.load(read_file_json)
        users = data
        req = request.POST
        checkLogin = req.get("login")
        checkPass = req.get("password")
        checkerror = True
        for i in users:
            if checkLogin == i['login']:
                print("Error")
                checkerror = False
                break
        if checkerror:
            ID = len(users) + 1
            newuser = {
                "login": checkLogin,
                "id": ID,
                "password": checkPass,
                #"Work": True,
                "position": "Moder"
            }
            users.append(newuser)
            with open('users.json', 'w', encoding='utf-8') as read_file_json:
                read_file_json.write(json.dumps(users, ensure_ascii=False, separators=(',', ': '), indent=2))

    return render(request, "addmoder.html", {})

def addtripdep(request, station_id):
    if request.POST:
        #id = id - 1
        #dock = dock - 1
        station_id=int(station_id)
        with open("json_data1.json", encoding='utf-8') as read_file_json:
            data = json.load(read_file_json)
        #Station = data
        req = request.POST
        checkName = req.get("Name")
        checkModel = req.get("Model")
        checkType = req.get("Type")
        checkClass = req.get("Class")
        checkDep = req.get("Departure")
        checkTimeDep = req.get("Time_dep")
        checkTimeArr = req.get("Time_arr")
        checkPrice = req.get("Price")
        Name = data['railway_station'][station_id]['name']
        #ID = len(Station['railway_station'][id]['trips'][0]['departure']) + 1
        #['railway_station'][station_id]['trips'][0]['departure']
        newtrip = {
                "train_name": checkName,
                "train_model": checkModel,
                "train_type": checkType,
                "class": checkClass,
                "departure": checkDep,
                "time_dep": checkTimeDep,
                "time_arr": checkTimeArr,
                "price": checkPrice
            }
        data['railway_station'][station_id]['trips'][0]['departure'].append(newtrip)
        with open('json_data1.json', 'w', encoding='utf-8') as read_file_json:
            read_file_json.write(json.dumps(data, ensure_ascii=False, separators=(',', ': '), indent=2))

    return render(request, "addtripdep.html", {})

def addtriparr(request, id):
    if request.POST:
        #id = id - 1
        #dock = dock - 1
        id=int(id)
        with open("json_data1.json", encoding='utf-8') as read_file_json:
            data = json.load(read_file_json)
        #Station = data
        req = request.POST
        checkName = req.get("Name")
        checkModel = req.get("Model")
        checkType = req.get("Type")
        checkClass = req.get("Class")
        checkArr = req.get("Arrival")
        checkTimeDep = req.get("Time_dep")
        checkTimeArr = req.get("Time_arr")
        checkPrice = req.get("Price")
        Name = data['railway_station'][id]['name']
        #ID = len(Station['railway_station'][id]['trips'][0]['departure']) + 1
        #['railway_station'][station_id]['trips'][0]['departure']
        newtrip = {
                "train_name": checkName,
                "train_model": checkModel,
                "train_type": checkType,
                "class": checkClass,
                "arrival": checkArr,
                "time_dep": checkTimeDep,
                "time_arr": checkTimeArr,
                "price": checkPrice
            }
        data['railway_station'][id]['trips'][0]['arrival'].append(newtrip)
        with open('json_data1.json', 'w', encoding='utf-8') as read_file_json:
            read_file_json.write(json.dumps(data, ensure_ascii=False, separators=(',', ': '), indent=2))

    return render(request, "addtriparr.html", {})



def moderatorlist(request):
    global Funcglobal
    if Funcglobal == "Admin":
        with open("users.json", encoding='utf-8') as read_file_json:
            data = json.load(read_file_json)
        users = data
        listmoderators = []
        for i in users:
            if i['position'] == "Moder":
                listmoderators.append(i)
        return render(request, "moderlist.html", {"moderators": listmoderators, "Func": Funcglobal})
    else:
        return redirect("/")

def userlist(request):
    global Funcglobal
    if Funcglobal == "Admin" or Funcglobal == "Moder":
        with open("users.json", encoding='utf-8') as read_file_json:
            data = json.load(read_file_json)
        users = data
        listusers = []
        for i in users:
            if i["position"] == "User":
                listusers.append(i)
        return render(request, "userlist.html", {"users": listusers, "Func":Funcglobal})
    else:
        return redirect("/")

def stationlist(request):
    global Funcglobal
    if Funcglobal == "none" or Funcglobal == "User":
        return redirect("/")
    with open("json_data1.json", encoding='utf-8') as read_file_json:
        data = json.load(read_file_json)
    Stations = data['railway_station']
    return render(request, "stationlist.html", {"Station": Stations, "Func": Funcglobal})

def stationlistuser(request):
    global Funcglobal
    if Funcglobal == "none":
        return redirect("/")
    with open("json_data1.json", encoding='utf-8') as read_file_json:
        data = json.load(read_file_json)
    Stations = data['railway_station']
    return render(request, "stationlistuser.html", {"Station": Stations, "Func": Funcglobal})

def point_trains_admin(request, station_id):
    with open("json_data1.json", encoding='utf-8') as read_file:
        data = json.load(read_file)
        station_id = int(station_id)
        station_name = data['railway_station'][station_id]['name']
        station_adress = data['railway_station'][station_id]['address']
        trips_dep = data['railway_station'][station_id]['trips'][0]['departure']
        trips_arr = data['railway_station'][station_id]['trips'][0]['arrival']
        dict_trips_1 = {  'name': station_name,
                         'id': station_id,
                        'address':station_adress,
                        'departure': trips_dep,
                        'arrival': trips_arr
                        }

    return render(request, 'point-trains-admin.html', dict_trips_1)


def logout(request):
    global Loginglobal
    global Passglobal
    global Funcglobal
    Loginglobal = "none"
    Passglobal = "none"
    Funcglobal = "none"
    request.session.clear()
    return redirect("/")

