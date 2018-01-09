from django.conf.urls import include, url
from django.contrib import admin
from loginsys import views

urlpatterns = [
    url(r'^login/', views.login, name='main'),
    url(r'^logout/', views.logout, name='main'),
    url(r'^register/$', views.register, name='register'),
]