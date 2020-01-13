from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm
# Create your views here.
def index(request):
    return render(request,'index.html')

def dashboardView(request):
    return render(request,'dashboard.html')

def login(request):
    return render(request,'registration/login.html')
def register(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UserCreationForm()
    context = {
        "form":form
    }
    return render(request,'registration/signup.html',context)
def logout(request):
    return render(request,'logout.html')