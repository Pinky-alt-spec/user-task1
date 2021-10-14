from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .forms import CreateUserForm, UserUpdateForm, ProfileUpdateForm

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

@login_required
def profile(request):
    return render(request, 'task/accounts/profile.html')


def profile_update(request):
    if request.method == 'POST':
        userform = UserUpdateForm(request.POST, instance=request.user)
        profileform = UserUpdateForm(request.POST, request.FILES, request.user.profile)
        if userform.is_valid() and profileform.is_valid():
            userform.save()
            profileform.save()
            return redirect('account-profile')
    else:
        userform = UserUpdateForm(instance=request.user)
        profileform = ProfileUpdateForm(instance=request.user.profile)
    context = {
        'userform': userform,
        'profileform': profileform,
    }
    return render(request, 'task/accounts/profile_update.html', context)


def login(request):
    return render(request, 'task/accounts/login.html')
