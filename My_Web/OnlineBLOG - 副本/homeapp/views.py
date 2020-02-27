from django.shortcuts import render
from django.shortcuts import HttpResponse
from django.shortcuts import redirect
from django.shortcuts import HttpResponseRedirect
from homeapp.models import BlogAcc
import time
import json
# Create your views here.

def timeNow():
    
    return time.strftime("%Y-%m-%d-:%M-%S-%Y", time.localtime())



def homePage(request):
    # print(request.COOKIES)
    account = request.get_signed_cookie('account', '', salt='{~a*#S$@[+-4=')
    
    if account == '':
        return render(request, 'home.html')

    info = {}
    info['account'] = account

    return render(request, 'home.html', info)

def logout(request):
    rep = HttpResponseRedirect('/')
    del request.COOKIES['account']
    print(request.COOKIES)

    request.session = {}
    print(request.session)

    return rep

def login(request):
    if request.POST:
        info = {}
        account = request.POST.get('account', None)
        password = request.POST.get('password', None)

        info =  {
            'account':account, 
        }

        request.session['account'] = account
        request.session['password'] = password

        rep = render(request, 'home.html', info)
        rep.set_signed_cookie('account', account, salt='{~a*#S$@[+-4=')

        return rep



def register(request):
    if request.POST:
        try:
            account = request.POST.get('account', None)
            password = request.POST.get('password', None)
            nickname = request.POST.get('nickname', None)



            BlogAcc.objects.create(account=account, password=password, 
                                    nickname=nickname)
            print('存储成功')
            print(account)
            print(password)
            info =  {
                'status': True,
                'result': '注册成功！',
                'nickname':nickname,
            }
        except:
            print('存储失败')
            info =  {
                "status": False,
                "result": '存储失败',
            }
        finally:
            return HttpResponse(json.dumps(info))
