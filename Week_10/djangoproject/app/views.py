from django.shortcuts import render, redirect
from django.contrib.auth.models import User, Group
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from app.models import UserProfile

# Create your views here.
# 跳转到index.html
def index(request):
    return render(request, 'index.html')

# 控制器函数添加一个用户User
def addUser(request):
    # 使用系统模型User实现对后台系统数据表auth_user的添加操作
    user = User.objects.create_user(username='admin', password='123')
    print('用户添加成功')
    return render(request, 'index.html')

# 跳转到details.html
@login_required
def details(request):
    return render(request, 'details.html')

# 登录业务处理
def mylogin(request):
    if request.POST:
        # 接收客户端请求数据
        username = request.POST.get('username', None)
        password = request.POST.get('password', None)
        phone = request.POST.get('phone', None)
        # 处理请求数据（数据库认证，session处理）
        user = authenticate(username=username, password=password)
        # 判断是否正确
        if user is not None:
            # 将用户信息添加到session会话中
            login(request, user)
            # 响应客户端
            return redirect('/app/details/')
        else:
            return render(request, 'login.html', {'errormsg':'登录验证失败'})
    else:
        return render(request, 'login.html')

# 退出业务实现
def mylogout(request):
    logout(request)
    return render(request, 'index.html')

# 创建用户的业务流程
def createUser(request):
    if request.POST:
        # 接收客户端请求数据
        username = request.POST.get('username', None)
        password = request.POST.get('password', None)
        phone = request.POST.get('phone', None)
        # 判断用户名是否存在
        user = User.objects.filter(username=username)
        if len(user) > 0:
            return render(request, 'createUser.html', {'error_msg':'登录用户名不能重复'})
        # 处理请求数据（向auth_user和app_userprofile表添加数据）
        # 向auth_user表添加数据
        user = User.objects.create_user(username=username, password=password)
        # 向app_userprofile表添加数据
        profile = UserProfile()
        profile.user_id = user.id
        profile.phone = phone
        profile.save()
        # 响应客户端
        return render(request, 'createUser.html', {'success_msg':'新用户创建成功.'})
    else:
        return render(request, 'createUser.html')

# 创建组
def createGroup(request):
    if request.POST:
        # 接收组名数据
        name = request.POST.get('name', None)
        group = Group.objects.filter(name=name)
        if len(group) > 0:
            return render(request, 'createGroup.html', {'error_msg':'组名不能重复'})
        # 处理组名数据（添加数据库）
        group = Group.objects.create(name=name)
        # 响应客户端
        return render(request, 'createGroup.html', {'success_msg':'组创建成功'})
    else:
        return render(request, 'createGroup.html')

# 查询全部租
def queryAllGroups(request):
    lstGroups = Group.objects.all()
    return render(request, 'showGroups.html', {'lstGroups':lstGroups})

# 向组中添加用户
def addGroupUsers(request, groupID):
    if request.POST:
        # 获取提交数据IDs
        chkUserIDs = request.POST.getlist('chkUserID', None)
        # 获取组对象
        group = Group.objects.get(id=groupID)
        for userID in chkUserIDs:
            user = User.objects.get(id = userID)
            group.user_set.add(user)
        return redirect('/app/group/queryall/')
    else:
        group = Group.objects.get(id=groupID)
        lstUsers = User.objects.all()
        ownerUsers = group.user_set.all()
        context = dict()
        context['group'] = Group.objects.get(id=groupID)
        context['lstUsers'] = lstUsers.difference(ownerUsers) # 求差集
        return render(request, 'addGroupUsers.html', context)

# 向组中删除用户
def removeGroupUsers(request, groupID):
    if request.POST:
        # 获取提交数据IDs
        chkUserIDs = request.POST.getlist('chkUserID', None)
        # 获取组对象
        group = Group.objects.get(id=groupID)
        for userID in chkUserIDs:
            user = User.objects.get(id = userID)
            group.user_set.remove(user)
        return redirect('/app/group/queryall/')
    else:
        group = Group.objects.get(id=groupID)
        context = dict()
        context['group'] = Group.objects.get(id=groupID)
        context['lstUsers'] = group.user_set.all()
        return render(request, 'removeGroupUsers.html', context)