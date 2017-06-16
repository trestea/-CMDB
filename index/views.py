from django.shortcuts import render,redirect
from django.contrib import admin
# Create your views here.
from django.views.decorators.csrf   import csrf_exempt,csrf_protect

from  django.shortcuts import render, redirect
from index import models


def auth(func):
    def inner(reqeust, *args, **kwargs):
        v = reqeust.COOKIES.get('user')
        if not v:
            return redirect('/login.html')
        return func(reqeust, *args, **kwargs)

    return inner



def index(request):  ##首页

    if request.session.get("is_login",None):
        return render(request, 'index.html')
    else:
        error_msg = "请登录"
        return render(request, 'login.html', {'error_msg': error_msg, })


def login(request):
    if request.method == "GET":
        error_msg = "请登录"
        return render(request, 'login.html', {'error_msg': error_msg, })
    if request.method == "POST":
          u = request.POST.get("user")
          p = request.POST.get("password")
          obj = models.UserInfo.objects.filter(username=u, password=p).first()
          if not obj:
              error_msg = "用户名或密码错误,请重试"
              return render(request, 'login.html', {'error_msg': error_msg, })
          else:
              request.session['user'] = u
              request.session['is_login'] =True
              return  redirect('/index.html')

    else:
        error_msg = "请登录"
        return render(request, 'login.html',{'error_msg': error_msg, })


def logout(requset):
    requset.session.clear()
    return  redirect('/login.html')
