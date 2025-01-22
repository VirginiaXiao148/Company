from django.shortcuts import render,redirect
from django.contrib.auth import logout as do_logout
from django.contrib.auth import authenticate
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login as do_login
from .models import Employee, Shift, Leave
from django import forms
from django.contrib import messages
from django.http import JsonResponse



# Create your views here.

def add_employee(request):
    if request.method == 'POST':
        name = request.POST['name']
        role = request.POST['role']
        Employee.objects.create(name=name, role=role)
        return redirect('employee_list')
    return render(request, 'management/add_employee.html')

def employee_list(request):
    employees = Employee.objects.all()
    return render(request, 'management/employee_list.html', {'employees': employees})

def add_shift(request):
    if request.method == 'POST':
        employee_list = Employee.objects.all()
        employee_id = employee_list.get(name=request.POST['employee_name']).id
        date = request.POST['shift_date']
        start_time = request.POST['shift_start']
        end_time = request.POST['shift_end']
        Shift.objects.create(employee_id=employee_id, date=date, start_time=start_time, end_time=end_time)
        return redirect('shift_list')
    employees = Employee.objects.all()
    return render(request, 'management/add_shift.html', {'employees': employees})

def shift_list(request):
    shifts = Shift.objects.all()
    shifts = sorted(shifts, key=lambda x: x.date)
    return render(request, 'management/shift_list.html', {'shifts': shifts})


def add_leave(request):
    if request.method == 'POST':
        employee_list = Employee.objects.all()
        employee_id = employee_list.get(name=request.POST['employee_name']).id
        date = request.POST['leave_date']
        reason = request.POST['leaveAction']
        Leave.objects.create(employee_id=employee_id, date=date, actions=reason)
        return redirect('leave_list')
    employees = Employee.objects.all()
    return render(request, 'management/add_leave.html', {'employees': employees})

def leave_list(request):
    leaves = Leave.objects.all()
    return render(request, 'management/leave_list.html', {'leaves': leaves})


def report_view(request):
    # Procesa los datos desde el modelo
    shifts = Shift.objects.all()
    data = {
        "labels": [shift.employee.name for shift in shifts],
        "dataset": [shift.end_time.hour - shift.start_time.hour for shift in shifts],  #Duración de los turnos
    }
    return render(request, 'management/report.html', {'data': JsonResponse(data).content.decode('utf-8')})


def get_shift_data(request):
    shifts = Shift.objects.all()
    data = {
        "labels": [shift.employee.name for shift in shifts],
        "dataset": [shift.end_time.hour - shift.start_time.hour for shift in shifts],
    }
    return JsonResponse(data)


















