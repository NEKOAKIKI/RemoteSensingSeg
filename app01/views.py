import json
from django.contrib import auth
from django.shortcuts import render, redirect
from django.core import serializers
from app01.models import *

# Create your views here.
def index(request):
    return render(request, 'index.html')


def logout(request):
    auth.logout(request)
    return redirect('/')


def home(request):
    user_info = UserInfo.objects.filter(nid=request.user.nid).first()
    user_list = UserInfo.objects.all()
    return render(request, 'home.html', locals())


def getstart(request):
    return render(request, 'getStart.html')


def userLur(request):
    return render(request, 'userLur.html')


def userupdate(request):
    nid = request.GET.get('nid')
    return render(request, 'userupdate.html', locals())


def userinfo(request):
    user_info = UserInfo.objects.filter(nid=request.user.nid).first()
    return render(request, 'userInfo.html', locals())


def upload(request):
    return render(request, 'upload.html', locals())

def record(request):
    record_list = Record.objects.filter(user=request.user.nid).order_by('create_date')[:7:-1]
    return render(request, 'record.html', locals())
