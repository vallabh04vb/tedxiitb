from django.contrib import admin
from django.urls import path
from tedapp import views
urlpatterns = [
 path("", views.index, name='index'),
 path('register', views.register, name='register'),
  path('Account',views.Account, name='Account'),
 path('speakers', views.speakers, name='speakers'),
  path('partners', views.partners, name='partners'),

]