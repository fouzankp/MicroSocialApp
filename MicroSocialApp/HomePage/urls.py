from django.urls import path
from . import views

urlpatterns = [
    path('', views.loginpage),
    #path('Rooms/', views.second_view),
    path('Feed', views.SignUp),
    path('login', views.LoginFeed),
    path('follow', views.followuser),
    path('UploadPost', views.PostUpload),
    path('LikePost', views.Like),
    
]
