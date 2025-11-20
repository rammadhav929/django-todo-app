from django.http import HttpResponse
from django.shortcuts import render
def ram(request):
    return render(request,'myfirst.html') 