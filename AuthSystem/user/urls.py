from django.urls import path 
from . import views

urlpatterns = [
    path('',views.index,name="home"),
    path('dashboard/',views.dashboardView,name="dashboard"),
    path('login/',views.login),
    path('register/',views.register),
    path('logout/',views.logout)
]