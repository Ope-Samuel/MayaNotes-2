from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns = [
    path("index/",views.index, name="index"),
    path("course/", views.course, name="course"),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('', views.loading, name='loading'),
    path('signup/', views.signup, name='signup'),
]