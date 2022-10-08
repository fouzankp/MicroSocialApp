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
    #print(request.POST)
    userid1 = request.POST['userid']
    pswd = request.POST['pswd']
    l = models.Login.objects.values('UserId','password')
    for i in l:
        if userid1 in i.values() and pswd in i.values():
            x = models.Login.objects.filter(UserId=userid1)
            fullname = x.values()[0].get('Fullname')
            return FeedPage(request, userid1)
    context = {'Invalid': True }
    return render(request, "loginorsignup.html", context)
    
def FeedPage(request, userid, followedid=''):
    k = models.Login.objects.filter(UserId=userid)[0]
    fullname = k.Fullname
    print('here')
    context = {'Username':fullname, 'Userid':userid, 'FollowedId':followedid }
    return render(request, "Feed.html", context)


def followuser(request):
    f = request.POST['follow']
    print(f)
    print(request.POST)
    u = request.POST['userid']
    print(u)
    l = models.Login.objects.values('UserId')
    print(l)
    context = {'Followed':False, 'Userid':f  }
    for i in l:
        if f in i.values():
            p = models.Followers(UserId=u , FollowUserId=u+'-'+f)
            p.save()
            return FeedPage(request, u, f)
            context = {'Followed':True, 'Userid':f }
    return FeedPage(request, u, 'False')