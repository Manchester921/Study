from django.shortcuts import render

# Create your views here.

def gotoIndex(request):
    return render(request,'index2.html')
