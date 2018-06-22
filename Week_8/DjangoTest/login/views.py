from django.shortcuts import render
from django.shortcuts import HttpResponse
from django.shortcuts import redirect


# Create your views here.

accountInfo = {'admin':'123',
               'Manchester':'921'}
onlineAccount = []

def gontoLogin(request):
    info = {}
    if 'account' in request.COOKIES:
        info['account'] = request.get_signed_cookie('account', salt='&1`)g@{a#4')
    if 'password' in request.COOKIES:
        info['password'] = request.get_signed_cookie('password', salt='&1`)g@{a#4')
    

    
    return render(request, 'login.html', info)



def gontoHome(request):
    if request.POST:
        info = {}
        info['account'] = request.POST.get('account', None)
        info['password'] = request.POST.get('password', None)
        if info['account'] in accountInfo and info['password'] == accountInfo[info['account']]:
            # if info['account'] not in onlineAccount:
                rep = render(request, 'home.html', info)
                rep.set_signed_cookie('account', info['account'], salt='&1`)g@{a#4')
                rep.set_signed_cookie('password', info['password'], salt='&1`)g@{a#4')
                request.session['account'] = info['account']
                request.session['password'] = info['password']
                onlineAccount.append(info['account'])
                return rep
        return redirect('/', {'msg':'用户名或密码错误'})
        return render(request, 'login.html', {'msg':'用户名或密码错误'})
        
    return redirect('/')








def logout(request):
    del request.session['account']
    del request.session['password']
    return redirect('/')