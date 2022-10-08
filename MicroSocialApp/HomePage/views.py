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
    context = {'SignedUp':True }
    return render(request, "loginorsignup.html", context)

def LoginFeed(request):
    print(request.POST)
    userid1 = request.POST['userid']
    pswd = request.POST['pswd']
    l = models.Login.objects.values('UserId')
    print(l)
    for i in l:
        if userid1 in i.values():
            x = models.Login.objects.filter(UserId=userid1)
            fullname = x.values()[0].get('Fullname')
            context = {'Username':fullname, 'Userid':userid1 }
            return render(request, "Feed.html", context)
    context = {'Invalid': True }
    return render(request, "loginorsignup.html", context)
    

def followuser(request):
    f = request.POST['follow']
    print(f)
    print(request.POST)
    u = request.POST['userid']
    print(u)
    l = models.Login.objects.values('UserId')
    for i in l:
        if f in i.values():
            p = models.Followers(UserId=u , FollowUserId=u+'-'+f)
            p.save()
            context = {'Followed':True, 'Userid':f }
        else:
            context = {'Followed':False, 'Userid':f  }
    return render(request, "followuser.html", context)