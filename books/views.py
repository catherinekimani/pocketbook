from django.shortcuts import render,redirect

from .forms import NewUserForm #newuserform class
from django.contrib.auth import login
from django.contrib import messages #import messages

# Create your views here.
def home(request):
    return render(request,'home.html')

def signup(request):
    form = NewUserForm()
    
    if request.method == 'POST':
        form = NewUserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    return render(request,'accounts/register.html',{'form':form})
    # 23979841

