from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def home(request):
    return render(request, 'home.html', {'name':'RISHI'})

def add(request):
    val1 = eval(request.POST["num1"])
    val2 = eval(request.POST["num2"])
    res = val1 + val2
    return render(request,"result.html",{"result":res})