from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def sub(request,num1,num2):
    return HttpResponse(int(num1) - int(num2))

def add(request,num1,num2):
    return HttpResponse(int(num1) + int(num2))
