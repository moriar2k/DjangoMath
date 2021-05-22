from django.urls import path
from . import views

urlpatterns = [
    path('sub/<num1>/<num2>', views.sub),
    path('add/<num1>/<num2>', views.add)
    path('div/<num1>/<num2>', views.div),
    path('mul/<num1>/<num2>', views.mul)
]

