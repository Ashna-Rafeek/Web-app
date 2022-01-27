import re
from django.shortcuts import render


def index(request):
    return render(request,"index.html")

def survey(request):
    return render(request,"survey.html")

def services(request):
    return render(request,"services.html")

def contact(request):
    return render(request,"contact.html")

def back(request):
    return render(request,"back.html")