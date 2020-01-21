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

def home(request):
    with open("json_data1.json", encoding='utf-8') as read_file:
        data = json.load(read_file)
        stations = data['railway_station']
        dict_stations = {'railway_station': stations}
    return render(request, 'HomePage.html', dict_stations)

def account(request):
    page = 'account.html'
    if "id" not in request.session:
        page = "404.html"
    position=request.session['position']
    return render(request, page, {'position':position})

def login(request):
    logForm = LoginForm(request.POST or None)
    error = 'None'
    global Loginglobal
    global Passglobal
    global Funcglobal
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
                return redirect("/account")

    return render(request, 'login.html', {'form': logForm,
                                          'error': error})

def point_trains(request, station_id):
    with open("json_data1.json", encoding='utf-8') as read_file:
        data = json.load(read_file)
        new_id = len(data['railway_station']) - 1
        station_id = int(station_id)
        if new_id < station_id:
            return redirect("/")
        station_name = data['railway_station'][station_id]['name']
        station_adress = data['railway_station'][station_id]['address']
        trips_dep = data['railway_station'][station_id]['trips'][0]['departure']
        trips_arr = data['railway_station'][station_id]['trips'][0]['arrival']
        dict_trips = {  'name': station_name,
                        'address':station_adress,
                        'departure': trips_dep,
                        'arrival': trips_arr}

    return render(request, 'point-trains.html', dict_trips)

def addstation(request):
    global Funcglobal
    if Funcglobal == "none" or Funcglobal == "User":
        return redirect("/")
    if request.POST:
        with open("json_data1.json", encoding='utf-8') as read_file_json:
            data = json.load(read_file_json)
        Station = data
        req = request.POST
        checkName = req.get("name")
        checkAddress = req.get("address")
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
    global Funcglobal
    if Funcglobal == "none" or Funcglobal == "User":
        return redirect("/")
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

def addusernew(request):
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

    return render(request, "addusernew.html", {})


@csrf_exempt
def addmoderator(request):
    global Funcglobal
    if Funcglobal == "none" or Funcglobal == "User" or Funcglobal == "Moder":
        return redirect("/")
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
                "position": "Moder"
            }
            users.append(newuser)
            with open('users.json', 'w', encoding='utf-8') as read_file_json:
                read_file_json.write(json.dumps(users, ensure_ascii=False, separators=(',', ': '), indent=2))

    return render(request, "addmoder.html", {})

def addtripdep(request, station_id):
    global Funcglobal
    if Funcglobal == "none" or Funcglobal == "User":
        return redirect("/")
    if request.POST:
        station_id=int(station_id)
        with open("json_data1.json", encoding='utf-8') as read_file_json:
            data = json.load(read_file_json)
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
    global Funcglobal
    if Funcglobal == "none" or Funcglobal == "User":
        return redirect("/")
    if request.POST:
        id=int(id)
        with open("json_data1.json", encoding='utf-8') as read_file_json:
            data = json.load(read_file_json)
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
    global Funcglobal
    if Funcglobal == "none":
        return redirect("/")
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

def error404(request):
    return render(request, '404.html', {})

def logout(request):
    global Loginglobal
    global Passglobal
    global Funcglobal
    Loginglobal = "none"
    Passglobal = "none"
    Funcglobal = "none"
    request.session.clear()
    return redirect("/")

