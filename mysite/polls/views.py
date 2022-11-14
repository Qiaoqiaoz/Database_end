import pymysql
from django.http import HttpResponse
from django.shortcuts import render
from .models import *


# Create your views here.


def toLogin_view(request):
    return render(request, 'login.html')


def Login_view(request):
    u = request.GET.get("user", '')
    p = request.GET.get("pwd", '')

    if u and p:
        c = User.objects.filter(user_id=u, user_password=p).count()
        if c >= 1:
            return HttpResponse("登录成功")
        else:
            return HttpResponse("账号密码错误")
    else:
        return HttpResponse("请输入正确的账号与密码")


def toRegister(request):
    return render(request, 'register.html')


def register_view(request):
    u = request.GET.get("user", '')
    p = request.GET.get("pwd", '')
    print(u)
    print(p)
    if u and p:
        user = User(user_name=u, user_password=p)
        user.save()
        return HttpResponse("注册成功"+u)
    else:
        return HttpResponse("请输入完整账号与密码"+u+p)


