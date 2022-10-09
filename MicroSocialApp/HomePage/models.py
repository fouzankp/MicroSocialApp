from email.policy import default
from django.db import models

# Create your models here.



class Login(models.Model):
    Fullname = models.CharField(max_length=20)
    UserId = models.CharField(primary_key=True,max_length=20)
    password = models.CharField(max_length=20)


class Followers(models.Model):
    UserId = models.CharField(max_length=20)
    FollowUserId = models.CharField(primary_key=True,max_length=40)

class Posts(models.Model):
    postid = models.CharField(primary_key=True,max_length=20)
    UserId = models.CharField(max_length=20,default='')
    TYPES = [('I', 'Image'),('V','Video')]
    type = models.CharField(max_length = 10,choices=TYPES)
    caption = models.CharField(max_length=50)

class PostLikes(models.Model):
    postid = models.CharField(max_length=20)
    likeduserid = models.CharField(max_length=40)
    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['postid','likeduserid'], name='unique_like_key')
        ]





