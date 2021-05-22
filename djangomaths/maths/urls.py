from django.urls import path
from . import views

urlpatterns = [
    path('<num1>/<num2>', views.sub),
    path('<num1>/<num2>', views.add)
]