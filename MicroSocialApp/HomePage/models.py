from django.db import models

# Create your models here.

#class Rooms(models.Model):
#    Roomno = models.IntegerField(primary_key=True)
#    TYPES = [('S', 'Single'),('D','Double')]
#    RoomType = models.CharField(choices=TYPES,max_length=10)
#    STYPES = [('C','CLEANED'),('N','NOTCLEANED'),('O','OCCUPIED')]
#    Status = models.CharField(default='C',choices=STYPES,max_length=10)
#    Checkin = models.DateTimeField(null=True)
#    Reserved = models.BooleanField(default=False)


class Login(models.Model):
    Fullname = models.CharField(max_length=20)
    UserId = models.CharField(primary_key=True,max_length=20)
    password = models.CharField(max_length=20)


#class Followers(models.Model):
#    UserId = models.CharField(primary_key=True,max_length=20)
#    FollowUserId = models.CharField(primary_key=True,max_length=20)
#
#class Posts(models.Model):
#    postid = models.CharField(primary_key=True,max_length=20)
#    filename = models.FileField
#    TYPES = [('I', 'Image'),('V','Video')]
#    type = models.CharField(max_length = 10,choices=TYPES)
#    caption = models.CharField(max_length=50)
#
#class PostLikes(models.Model):
#    postid = models.CharField(primary_key=True,max_length=20)
#    likeduserid = models.CharField(primary_key=True,max_length=20)







