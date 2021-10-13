from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from .forms import CreateUserForm

# Create your views here.

def register(request):
    if request.method == 'POST':   
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('account-login')
    else:
        form = CreateUserForm()
       
    context = {
        'form': form
    }
    return render(request, 'task/accounts/register.html', context)


def login(request):
    return render(request, 'task/accounts/login.html')
