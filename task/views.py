from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, 'task/index.html')

def current(request):
    return render(request, 'task/current.html')

def completed(request):
    return render(request, 'task/completed.html')

def deleted(request):
    return render(request, 'task/deleted.html')

def profile(request):
    return render(request, 'task/profile.html')
