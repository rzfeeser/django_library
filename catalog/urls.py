from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),     # new line to add
]

