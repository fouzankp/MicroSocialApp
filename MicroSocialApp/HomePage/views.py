import imp
from re import L
from django.shortcuts import render, redirect
from django.http import HttpResponse
from . import models
# Create your views here.

def loginpage(request):
    context = { }
    return render(request, "loginorsignup.html", context)

def SignUp(request):
    fullname = request.POST['Fullname']
    userid = request.POST['userid']
    pswd = request.POST['pswd']
    p = models.Login(Fullname=fullname, UserId=userid, password=pswd)
    l = models.Login.objects.values('UserId')
    for i in l:
        if userid in i.values():
            context = {'Existing':True }
            return render(request, "loginorsignup.html", context)
    p.save()
    print(fullname)
    context = { }
    return redirect(LoginFeed)

def LoginFeed(request):
    print(request.POST)
    userid1 = request.POST['userid']
    pswd = request.POST['pswd']
    l = models.Login.objects.values('UserId')
    print(l)
    for i in l:
        if userid1 in i.values():
            context = { }
            return render(request, "Feed.html", context)
    context = {'Invalid': True }
    return render(request, "loginorsignup.html", context)
    