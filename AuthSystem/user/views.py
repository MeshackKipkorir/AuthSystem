from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request,'index.html')

def dashboardView(request):
    return render(request,'dashboard.html')

def login(request):
    return render(request,'registration/login.html')
def register(request):
    return render(request,'registration/signup.html')
def logout(request):
    return render(request,'logout.html')