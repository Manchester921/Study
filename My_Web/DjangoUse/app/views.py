from django.shortcuts import render, HttpResponse, redirect, HttpResponseRedirect
from django.contrib.auth.models import User, Group
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from app.models import UserProfile
import json
import random
# Create your views here.

def index(request):
    print(request.POST)
    if '_auth_user_id' in request.session:
        auth_user_id = request.session['_auth_user_id']
        userName = User.objects.get(id = auth_user_id)
        return render(request, 'index.html', {'userName':userName})
        
    
    # User.objects.create_user(username='admin', password='123')
    return render(request, 'index.html')

def mylogin(request):
    print(request.POST)
    if request.POST:
        username = request.POST.get('LoginUserName', None)
        password = request.POST.get('LoginPassWord', None)
        user = authenticate(username=username, password=password)
        if user is not None:
            info = {
                "status": True,
                'username':username, 
            }
            login(request, user)
            print(dict(request.session))
            print(request.session['_auth_user_id'])
            return HttpResponse(json.dumps(info,ensure_ascii=False),
                                content_type='application/json')
        else:
            
            info = {
                "status": False,
                'msg':'用户名或密码错误！'
            }
            return HttpResponse(json.dumps(info,ensure_ascii=False),
                                content_type='application/json')
    else:
        return render(request, 'index.html', {"needLogin":1})

def myRegister(request):
    print(request.POST)
    
    if request.POST:
        username = request.POST.get('RegisterUserName', None)
        password = request.POST.get('RegisterPassWord', None)
        phone = request.POST.get('RegisterPhone', None)
        user = User.objects.filter(username=username)
        print(user)
  
        if len(user) > 0:
            info = {
                "status": False,
                'msg':'登录用户名不能重复！'
            }
            print('创建失败')
            return HttpResponse(json.dumps(info,ensure_ascii=False),
                                content_type='application/json')
        
        user = User.objects.create_user(username=username, password=password)

        profile = UserProfile()
        profile.user_id = user.id
        profile.phone = phone
        profile.save()
        print('创建成功')
        
        login(request, user)

        info = {
            "status": True,
            'username':username, 
        }
            
        return HttpResponse(json.dumps(info,ensure_ascii=False),
                            content_type='application/json')

def mylogout(request):
    logout(request)
    return redirect('/')

@login_required
def showGroups(request):
    lstGroups = Group.objects.all()
    return render(request, 'groups.html', {'lstGroups':lstGroups})


# @login_required
def createGroup(request):
    print(request.POST)
    if request.POST:
        name = request.POST.get('createGroups', None)
        group = Group.objects.filter(name=name)
        print('name:',name,'group:',group)
        if len(group) > 0:
            info = {
                "status": False,
                'createGroupErrormsg':'组名不能重复', 
            }
            return  HttpResponse(json.dumps(info,ensure_ascii=False),
                                content_type='application/json')
        group = Group.objects.create(name=name)
        info = {
            "status": True,
            'createGroupsuccessmsg':'组创建成功',
        }
        return  HttpResponse(json.dumps(info,ensure_ascii=False),
                                content_type='application/json')

def addGroupUsers(request, groupID):
    if request.POST:
        # 获取提交数据IDs
        chkUserIDs = request.POST.getlist('chkUserID', None)
        # 获取组对象
        group = Group.objects.get(id=groupID)
        for userID in chkUserIDs:
            user = User.objects.get(id = userID)
            group.user_set.add(user)

    group = Group.objects.get(id=groupID)
    lstUsers = User.objects.all()
    ownerUsers = group.user_set.all()
    info = {}
    info['group'] = Group.objects.get(id=groupID)
    info['lstUsers'] = lstUsers.difference(ownerUsers)
    return render(request, 'addGroupUsers.html', info)


def removeGroupUsers(request, groupID):
    if request.POST:
        # 获取提交数据IDs
        chkUserIDs = request.POST.getlist('chkUserID', None)
        # 获取组对象
        group = Group.objects.get(id=groupID)
        for userID in chkUserIDs:
            user = User.objects.get(id = userID)
            group.user_set.remove(user)
        
    group = Group.objects.get(id=groupID)
    info = {}
    info['group'] = Group.objects.get(id=groupID)
    info['lstUsers'] = group.user_set.all()
    return render(request, 'removeGroupUsers.html', info)

