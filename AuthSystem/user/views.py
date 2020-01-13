from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
# Create your views here.
def index(request):
    return render(request,'index.html')
@login_required
def dashboardView(request):
    return render(request,'dashboard.html')

def register(request):
    form = UserCreationForm()
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
