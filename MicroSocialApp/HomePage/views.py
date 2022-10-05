import imp
from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def loginpage(request):
    context = { }
    return render(request, "loginorsignup.html", context)


