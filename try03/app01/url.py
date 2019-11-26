from django.urls import path
from . import views

urlpatterns = [
    path('result/', views.crawler),
    path('', views.command),
]