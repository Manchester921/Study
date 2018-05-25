from django.shortcuts import render
from django.shortcuts import HttpResponse
from django.shortcuts import redirect

# Create your views here.

def checkCookie(req):

    account = req.get_signed_cookie('account', None, salt='{~a*#S$@[+-4=')
    if account == None:
        return None
    password = req.get_signed_cookie('password', None, salt=account+'{~a*#S$@[+-4=')

    if password == None:
        return None
    return {'account':account}




def gotoTest(request):
    return render(request, 'test.html')
def gotoAdds(request, num1, num2):
    return HttpResponse('结果为：%s'%(num1+num2))







def gotoLogin(request):
    account = request.get_signed_cookie('account', None, salt='{~a*#S$@[+-4=')
    rememberMe = request.COOKIES.get('rememberMe', 'off')
    # print(request.COOKIES)
    
    info = {}
    if account:
        if 'rememberMe' in request.COOKIES and request.COOKIES['rememberMe'] == 'on':
            password = request.get_signed_cookie('password', None, salt=account+'{~a*#S$@[+-4=')
            info['password'] = password
            if password == None:
                del info['password']
                


        info['account'] = account
        info['rememberMe'] = rememberMe
        # print(request.COOKIES)

        return render(request, 'login.html', info)
    
    if 'password' in request.COOKIES:
        del request.COOKIES['password']
        # print('password')
    # print(request.COOKIES)
    return render(request, 'login.html')



def gotoRegister(request):
    return render(request, 'register.html')

def register(request):
    if request.POST:
        info= {}
        info['account'] = request.POST.get('account', '')
        info['password'] = request.POST.get('password', '')
        info['name'] = request.POST.get('name', '')
        info['userPic'] = request.POST.get('userPic', '')
        info['quote'] = request.POST.get('quote', '')
        return render(request, 'register.html', info)
    else:
        return render(request, 'register.html')

def blogLogin(request):

    accouunt = checkCookie(request)
    if accouunt != None:
        return render(request, 'blog.html', accouunt)
    elif request.POST:
        info = {}
        account = request.POST.get('account', None)
        password = request.POST.get('password', None)
        rememberMe = request.POST.get('rememberMe', None)

        info =  {
            'account':account, 
            'password':password, 
            'rememberMe':rememberMe, 
        } 
        request.session['account'] = account

        rep = render(request, 'blog.html', info)
        rep.set_signed_cookie('account', account, salt='{~a*#S$@[+-4=', expires=100)
        if rememberMe:
            rep.set_signed_cookie('password', password, salt=account+'{~a*#S$@[+-4=', expires=100)
            rep.set_cookie('rememberMe', rememberMe)
        else:
            if 'password' in request.COOKIES:
                del request.COOKIES['password']
        return rep
    else:
        if 'password' in request.COOKIES:
            del request.COOKIES['password']
        return redirect('/')
        # return render(request, 'blog.html')


def logout(request):
    print(request.COOKIES)
    
    if 'password' in request.COOKIES:
        del request.COOKIES['password']
        print(request.COOKIES)
    
    return redirect('/')