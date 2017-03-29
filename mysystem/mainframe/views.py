# coding:utf-8
from django.shortcuts import render,render_to_response
from django.http import HttpResponseRedirect
from .models import *
# Create your views here.

def home(req):
    return render_to_response("home.html")

def login(req):
    return render_to_response("login.html")

def registration(req):
    return render_to_response("registration.html")

def host_management(req):
    return render_to_response("host_management.html")

def user_management(req):
    return render_to_response("user_management.html")

def personal_center(req):
    return render_to_response("personal_center.html")
def add(req):
    return render_to_response("add.html")

def index(req):
    username=req.COOKIES.get('username',"")
    computers = Computer.objects.all()
    return render_to_response("home.html",{"computers":computers, 'username':username})

def acc_regist(request):
    username = request.POST.get('username')
    password = request.POST.get('password')
    repassword = request.POST.get('repassword')
    print username, password, repassword
    return render_to_response("home.html")
    if users.object.all().filter(username = username):
        return render_to_response("用户已存在")
    else:
        if password == repassword:
            User.object.create(username = username,password = password)
            username = request.COOKIES.get('username', "")
            computers = Computer.objects.all()
            return render_to_response("registration.html", {"computers": computers, 'username': username})
        else:
            return render_to_response("注册成功")

def acc_login(req):
    username = req.POST.get('username')
    password = req.POST.get('password')
    if User.objects.all().filter(username=username):
        user= User.objects.all().get(username=username)
        if password==password:
            response = HttpResponseRedirect('/')
            response.set_cookie('username', username, 3600)
            return response
        else:
            return render_to_response("home.html", {'error': '恭喜你活下来了'})

    else:
        return render_to_response("login.html", {'error': '去死哦'})

def logout(req):
    response = HttpResponseRedirect('/')
    response.delete_cookie('username')
    return response



