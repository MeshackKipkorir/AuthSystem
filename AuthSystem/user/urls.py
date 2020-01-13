from django.urls import path 
from . import views
from django.contrib.auth.views import LoginView,LogoutView
app_name = 'user'
urlpatterns = [
    path('',views.index,name="home"),
    path('dashboard/',views.dashboardView,name="dashboard"),
    path('login/',LoginView.as_view(),name="login"),
    path('register/',views.register),
    path('logout/',LogoutView.as_view(),name="logout")
]