from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.
def div(request, num1, num2):
    return HttpResponse(int(num1) / int(num2))


def mul(request, num1, num2):
    return HttpResponse(int(num1) * int(num2))