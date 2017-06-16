#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Create your views here.
from  django.shortcuts import HttpResponse
from  django.shortcuts import render, redirect
from jigui import models
from django.views.decorators.csrf   import csrf_exempt,csrf_protect
import index




def jigui(request):  ##首页
    jigui = models.JiguiInfo.objects.filter(id__gt=0)
    return render(request, 'jigui/jigui.html',{"jigui_list": jigui,})

def add(request):
    if request.method == "POST":
        name1 = request.POST.get('name', None)
        jq1 = request.POST.get('jq', None)
        zy1 = request.POST.get('zy', None)
        ziy1 = request.POST.get('ziy', None)
        zs1 = request.POST.get('zs', None)
        zb1 = request.POST.get('zb', None)
        sh1 = request.POST.get('sh', None)
        xz1 = request.POST.get('xz', None)
        dx1 = request.POST.getlist('dx')
        yong1 = request.POST.get('yong')


        obj = models.JiguiInfo.objects.create(name_id=name1, jq=jq1, zy=zy1, ziy=ziy1, zs=zs1, zb=zb1, sh=sh1,xz=xz1,yong=yong1)
        obj.d.add(*dx1)

        msg = "添加成功"
        groupid = index.models.JifangGroup.objects.all()
        dx = models.dx.objects.all()
        return render(request, 'jigui/add.html', {"group_id":groupid,'msg': msg ,"dx_list":dx})
    else:
        groupid = index.models.JifangGroup.objects.all()
        dx = models.dx.objects.all()
        return render(request, 'jigui/add.html', {"group_id":groupid,"dx_list":dx})


def xiangxi(request, nid):  #详细页面
    jigui = models.JiguiInfo.objects.filter(id=nid).first()
    obj = models.JiguiInfo.objects.get(id=nid)
    dx = obj.d.all()
    return render(request, 'jigui/xiangxi.html', {"xiangxi_info": jigui,"dx":dx})

def jigui_del(request, nid):  #删除
    models.JiguiInfo.objects.filter(id=nid).delete()
    return redirect('/jigui/jigui.html')



def jigui_edit(request, nid):   #编辑
    if request.method == "GET":
        obj = models.JiguiInfo.objects.filter(id=nid).first()
        groupid = index.models.JifangGroup.objects.all()
        obj = models.JiguiInfo.objects.get(id=nid)
        dx = obj.d.all()
        dx1 = models.dx.objects.all()

        return render(request, 'jigui/jiguiedit.html', {'obj': obj,"group_id": groupid,"dx_list":dx,"dx_list1":dx1})

    elif request.method == "POST":
        name1 = request.POST.get('name', None)
        jq1 = request.POST.get('jq', None)
        zy1 = request.POST.get('zy', None)
        ziy1 = request.POST.get('ziy', None)
        zs1 = request.POST.get('zs', None)
        zb1 = request.POST.get('zb', None)
        sh1 = request.POST.get('sh', None)
        xz1 = request.POST.get('xz', None)
        dx1 = request.POST.getlist('dx')
        yong1 = request.POST.get('yong')

        obj = models.JiguiInfo.objects.filter(id=nid).first()
        obj.name_id=name1
        obj.jq=jq1
        obj.zy=zy1
        obj.ziy=ziy1
        obj.zs=zs1
        obj.zb=zb1
        obj.sh=sh1
        obj.xz=xz1
        obj.yong=yong1
        obj.save()
        obj1 = models.JiguiInfo.objects.get(id=nid)
        obj1.d.set(dx1)

        return redirect('/jigui/jigui.html')
    else:
        return redirect('/index.html')


