from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, 'task/dashboard/index.html')

def current(request):
    return render(request, 'task/dashboard/current.html')

def completed(request):
    return render(request, 'task/dashboard/completed.html')

def deleted(request):
    return render(request, 'task/dashboard/deleted.html')

def profile(request):
    return render(request, 'task/accounts/profile.html')
