from datetime import datetime, timedelta
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
    leaves = sorted(leaves, key=lambda x: x.date)
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








# Define las vacaciones
VACACIONES = [
    datetime(2025, 1, 1), # Día de la Independencia
    datetime(2025, 1, 6), # Día de Reyes
    datetime(2025, 4, 17), # Jueves Santo
    datetime(2025, 4, 18), # Viernes Santo
    datetime(2025, 5, 1), # Fiesta del Trabajo
    datetime(2025, 5, 2), # Fiesta de la Comunidad de Madrid
    datetime(2025, 7, 25), # dia del apostol Santiago
    datetime(2025, 8, 15), # Asunción de la Virgen
    datetime(2025, 9, 15), # Cristo de la misericordia
    datetime(2025, 11, 1), # Día de todos los santos
    # datetime(2025, 11, 9), # Día de la Almudena
    datetime(2025, 12, 6), # Día de la Constitución
    datetime(2025, 12, 8), # Día de la Inmaculada Concepción
    datetime(2025, 12, 25), # Navidad
    datetime(2025, 12, 26), # Fiesta Local Fuenlabrada
]

# Función para obtener todas las fechas entre dos fechas excluyendo fines de semana y vacaciones
def obtener_fechas_excluyendo_fines_de_semana_y_vacaciones(inicio, fin):
    fechas = []
    delta = timedelta(days=1)
    while inicio <= fin:
        if inicio.weekday() < 5 and inicio not in VACACIONES:  # 0-4 son lunes-viernes
            fechas.append(inicio)
        inicio += delta
    return fechas

def guardar_turnos_noviembre_diciembre(request):
    if request.method == 'POST':
        # Obtener el empleado
        employee = Employee.objects.get(id=request.POST['employee_id'])
        
        # Definir el rango de fechas
        inicio = datetime(2025, 3, 8)
        fin = datetime(2025, 3, 25)
        
        # Obtener las fechas excluyendo fines de semana y vacaciones
        fechas = obtener_fechas_excluyendo_fines_de_semana_y_vacaciones(inicio, fin)
        
        # Crear turnos para cada fecha
        for fecha in fechas:
            Shift.objects.create(
                employee=employee,
                date=fecha,
                start_time=datetime.strptime('08:00', '%H:%M').time(),
                end_time=datetime.strptime('17:30', '%H:%M').time()
            )
        
        return redirect('shift_list')
    
    employees = Employee.objects.all()
    return render(request, 'management/guardar_turnos.html', {'employees': employees})









