from django.shortcuts import redirect, render
from .models import *
from django.contrib.auth.decorators import login_required
from .forms import CurrentForm
from django.contrib import messages

import datetime
import xlwt
from django.http import HttpResponse
from django.contrib.auth.models import User


# Create your views here.

@login_required
def index(request):
    comp_tasks_count = Current.objects.filter(status='Completed').count()
    del_tasks_count = Current.objects.filter(status='Deleted').count()
    curr_tasks_count = Current.objects.filter(status='Current').count()
    context = {
        'comp_tasks_count': comp_tasks_count,
        'del_tasks_count': del_tasks_count,
        'curr_tasks_count': curr_tasks_count,
    }
    return render(request, 'task/dashboard/index.html', context)


def about(request):
    
    return render(request, 'task/dashboard/about.html')

@login_required
def current(request):
    curr_tasks = Current.objects.filter(status='Current')
    curr_tasks_count = curr_tasks.count()

    del_tasks_count = Current.objects.filter(status='Deleted').count()
    comp_tasks_count = Current.objects.filter(status='Completed').count()
   
    if request.method == "POST":
        form = CurrentForm(request.POST)
        if form.is_valid():
            form.save()
            task_name = form.cleaned_data.get('task')
            messages.success(request, f'{task_name} has been added')
            
            return redirect('dashboard-current')
    else:
        form = CurrentForm()

    context = {
        'comp_tasks_count': comp_tasks_count,
        'del_tasks_count': del_tasks_count,
        'curr_tasks': curr_tasks,
        'curr_tasks_count': curr_tasks_count,
        'form': form,
    }
    return render(request, 'task/dashboard/current.html', context)


# Current update and delete
def current_delete(request, pk):
    curr_del = Current.objects.get(id=pk)
    if request.method == "POST":
        curr_del.delete()
        return redirect('dashboard-current')

    return render(request, 'task/dashboard/current_delete.html')


def current_update(request, pk):
    curr_up = Current.objects.get(id=pk)
    if request.method == "POST":
        form = CurrentForm(request.POST, instance=curr_up)
        if form.is_valid():
            form.save()
            return redirect('dashboard-current')
    else:
        form = CurrentForm(instance=curr_up)
    context = {
        'form': form,
    }
    return render(request, 'task/dashboard/current_update.html', context)


# Completed update and delete
def completed_delete(request, pk):
    comp_del = Current.objects.get(id=pk)
    if request.method == "POST":
        comp_del.delete()
        return redirect('dashboard-current')

    return render(request, 'task/dashboard/completed_delete.html')


def completed_update(request, pk):
    comp_up = Current.objects.get(id=pk)
    if request.method == "POST":
        form = CurrentForm(request.POST, instance=comp_up)
        if form.is_valid():
            form.save()
            return redirect('dashboard-current')
    else:
        form = CurrentForm(instance=comp_up)
    context = {
        'form': form,
    }
    return render(request, 'task/dashboard/completed_update.html', context)



@login_required
def completed(request):
    comp_tasks = Current.objects.filter(status='Completed')
    comp_tasks_count = comp_tasks.count()

    del_tasks_count = Current.objects.filter(status='Deleted').count()
    curr_tasks_count = Current.objects.filter(status='Current').count()


    
    context = {
        'comp_tasks': comp_tasks,
        'comp_tasks_count': comp_tasks_count,
        'del_tasks_count': del_tasks_count,
        'curr_tasks_count': curr_tasks_count,
    }
    return render(request, 'task/dashboard/completed.html', context)


@login_required
def deleted(request):
    del_tasks = Current.objects.filter(status='Deleted')
    del_tasks_count = del_tasks.count()
    comp_tasks_count = Current.objects.filter(status='Completed').count()
    curr_tasks_count = Current.objects.filter(status='Current').count()

    context = {
        'del_tasks': del_tasks,
        'comp_tasks_count': comp_tasks_count,
        'del_tasks_count': del_tasks_count,
        'curr_tasks_count': curr_tasks_count,
    }
    
    return render(request, 'task/dashboard/deleted.html', context)


def export_excel(request):
    response=HttpResponse(content_type='application/ms-excel')
    response['Content-Disposition'] = 'attachment; filename=current.xls' + \
        str(datetime.datetime.now())+'.xls'
  
    wb = xlwt.Workbook(encoding='utf-8')
    ws = wb.add_sheet('Current Tasks')
    row_num = 0

    font_style = xlwt.XFStyle()
    font_style.font.bold = True

    columns = ['task', 'date', 'status', ]

    for col_num in range(len(columns)):
        ws.write(row_num, col_num, columns[col_num], font_style) # at 0 row 0 column 

    curr_tasks = Current.objects.filter(status='Current').values_list('task', 'date', 'status')
  
    for row in curr_tasks:
        row_num += 1
        for col_num in range(len(row)):
            ws.write(row_num, col_num, row[col_num], font_style)
        
    wb.save(response)
    

    comp_tasks = Completed.objects.filter(status='Completed').values_list('task', 'date', 'status')
    for row in comp_tasks:
        row_num += 1
        for col_num in range(len(row)):
            ws.write(row_num, col_num, row[col_num], font_style)
        
    wb.save(response)
    return response
    