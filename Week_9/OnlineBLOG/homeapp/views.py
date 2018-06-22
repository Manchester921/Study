from django.shortcuts import render
from django.shortcuts import HttpResponse
from django.shortcuts import redirect
from django.shortcuts import HttpResponseRedirect
from homeapp.models import BlogAcc
import time
import json
import random
# Create your views here.


def homePage(request):
    # print(request.COOKIES)
    account = request.COOKIES.get('account', '')

    if account == '':
        return render(request, 'home.html')

    info = {}
    info['account'] = account
    
    if 'account' in request.session and  'password' in request.session:
        result = BlogAcc.objects.filter(account=request.session['account'])
        if len(result)>0:
            result = result[0]
            if result.password == request.session['password']:
                info['nickname'] = result.nickname
    print(info)
    return render(request, 'home.html', info)


def logout(request):
    del request.session['account']
    del request.session['password']
    del request.session['nickname']

    return redirect('/')


def login(request):
    if request.POST:
        try:
            account = request.POST.get('loginAccount', None)
            password = request.POST.get('loginPassword', None)
            print('account:'+account,'password:'+password)
            
            result = BlogAcc.objects.filter(account=account)

            # print('result[0]:',result[0])
            
            if len(result)>0:
                result = result[0]
 
                if result.password == password:
                    # print(result.nickname)
                    
                    info =  {
                        "status": True,
                        'nickname':result.nickname, 
                    }
                    request.session['account'] = account
                    request.session['password'] = password
                    request.session['nickname'] = result.nickname
                    print('session:',request.session)
                    rep = HttpResponse(json.dumps(info,ensure_ascii=False),
                                content_type='application/json')
                    return rep

            info = {
                    "status": False,
                }

        except:
            info =  {
                    "status": False,
                }
        finally:
            # print(info)
            return HttpResponse(json.dumps(info,ensure_ascii=False),
                                content_type='application/json')













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
            print(nickname)
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
            return HttpResponse(json.dumps(info,ensure_ascii=False),
                                content_type='application/json')




def regAccOnly(request):
    if request.POST:
        try:
            regaccount = request.POST.get('regaccount', None)
            result = BlogAcc.objects.filter(account=regaccount)
            # print(regaccount)
            # print(list(result))
            if len(result)>0:
                # print('False')
                return HttpResponse(False)
            else:
                # print('True')
                return HttpResponse(True)
        except:
            return HttpResponse(False)


def VerCodesend(request):
    VerCode = str(random.randint(100000,999999))
    print(VerCode)
    return HttpResponse(VerCode)

