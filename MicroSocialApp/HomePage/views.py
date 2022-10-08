from django.shortcuts import render, redirect
from django.http import HttpResponse
from . import models
from .forms import UploadFileForm
from django.core.files.storage import FileSystemStorage
import datetime
import os
from django.conf import settings
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

    #followersposts
    f = models.Followers.objects.filter(UserId=userid)
    l=len(userid)
    postlist = []
    for x in f:
        i = x.FollowUserId
        i = i[l+1:]
        p = models.Posts.objects.filter(UserId=i)
        for y in p:
            postset = {}
            postset['PostId'] = y.postid
            postset['UserId'] = i
            postset['Caption'] = y.caption
            like = models.PostLikes.objects.filter(postid=y.postid)
            postset['likes'] = len(like)
            postset['type'] = y.type
            fs = FileSystemStorage()
            img = fs.open(y.postid)
            print(img)
            print(fs.url(y.postid))
            postset['img'] = fs.url(y.postid)
            postlist.append(postset)
    #print(postlist)        
    #print(dir(fs))
    path = settings.MEDIA_ROOT
    img_list = os.listdir(path + "/")
    print(path)
    print(img_list)
    context = {'Username':fullname, 'Userid':userid, 'FollowedId':followedid, 'Posts':postlist }
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
    return FeedPage(request, u, 'False')


def PostUpload(request):
    u = request.POST['userid']
    caption = request.POST['caption']
    myfile = request.FILES['fileid']
    s = datetime.datetime.now()
    d = s.strftime('%y%m%d%H%M%S')
    splittxt = os.path.splitext(myfile.name)
    ext = splittxt[len(splittxt)-1]
    d = d + ext
    ftype = myfile.content_type[0].upper()
    fs = FileSystemStorage()
    filename = fs.save(d, myfile)
    uploaded_file_url = fs.url(filename)
    p = models.Posts(postid=d, UserId=u ,type=ftype,caption=caption)
    p.save()

    return FeedPage(request, u)