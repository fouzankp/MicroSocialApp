from django.urls import path
from . import views

urlpatterns = [
    path('', views.loginpage),
    #path('Rooms/', views.second_view),
]
