from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.contrib.auth.views import LoginView, LogoutView
from .models import Job

# Create your views here.
def home(request):
    return render(request,'portal/home.html')

def index(request):
    jobs = Job.objects.all()
    return render(request,'portal/index.html',{'jobs':jobs})


def register_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'portal/register.html',{'form':form})

def login_view(request):
   
    if request.user.is_authenticated:
        return redirect('home') 
    else:
        return LoginView.as_view(template_name='portal/login.html')(request)

def logout_view(request):
    return LogoutView.as_view(next_page=reverse_lazy('login'))(request)



