from . import views
from django.urls import path

urlpatterns = [
    path('div/<num1>/<num2>', views.div),
    path('mul/<num1>/<num2>', views.mul)
]

