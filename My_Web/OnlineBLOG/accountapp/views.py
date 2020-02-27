from django.shortcuts import render
from django.shortcuts import HttpResponse
from django.shortcuts import redirect
from django.shortcuts import HttpResponseRedirect
from homeapp.models import BlogAcc,BlogInfo

# Create your views here.

def accountLogin(request, account):
    info = {}
    if 'account' in request.session and  'password' in request.session:
        result = BlogAcc.objects.filter(account=account)
        if len(result)>0:
            result = result[0]
            if result.account == request.session['account'] and result.password == request.session['password']:
                info['account'] = account
                info['nickname'] = result.nickname
    return info





def accountBlogHome(request, account):

    info = {}

    info.update(accountLogin(request, account))
    if info:
        return render(request, 'account.html', info)

    return redirect('/')
                    
                    



def gotoPublishBlog(request, account):
    info = {}

    info.update(accountLogin(request, account))
    if info:
        return render(request, 'accPub.html', info)

    return redirect('/')
                    
def publishBlog(request, account):
    if request.POST:
        try:
            BlogPubTitle = request.POST.get('BlogPubTitle', None)
            BlogPubContent = request.POST.get('BlogPubContent', None)
            print('BlogPubTitle:'+BlogPubTitle,'BlogPubContent:'+BlogPubContent)
            
            BlogInfo.objects.Create(title=BlogPubTitle, content=  BlogPubContent )


            info = {}
            info.update(accountLogin(request, account))
            if info:
                return render(request, 'accPub.html', info)

            # return redirect(account+'/')
        except:
            info = {}

            info.update(accountLogin(request, account))
            if info:
                return render(request, 'accPub.html', info)


             

