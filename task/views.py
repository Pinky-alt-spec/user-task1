from django.shortcuts import redirect, render
from .models import Current
from django.contrib.auth.decorators import login_required
from .forms import CurrentForm


# Create your views here.

@login_required
def index(request):
    return render(request, 'task/dashboard/index.html')

@login_required
def current(request):
    tasks = Current.objects.all()
    if request.method == "POST":
        form = CurrentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('dashboard-current')
    else:
        form = CurrentForm()

    context = {
        'tasks': tasks,
        'form': form,
    }
    return render(request, 'task/dashboard/current.html', context)

def current_delete(request, pk):
    task = Current.objects.get(id=pk)
    if request.method == "POST":
        task.delete()
        return redirect('dashboard-current')

    return render(request, 'task/dashboard/current_delete.html')


@login_required
def completed(request):
    return render(request, 'task/dashboard/completed.html')

@login_required
def deleted(request):
    return render(request, 'task/dashboard/deleted.html')

