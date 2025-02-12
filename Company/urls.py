"""
URL configuration for Company project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from management import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('management/employees/add/', views.add_employee, name='add_employee'),
    path('management/employees/list/', views.employee_list, name='employee_list'),
    path('management/shifts/add/', views.add_shift, name='add_shift'),
    path('management/shifts/guardar-turnos/', views.guardar_turnos_noviembre_diciembre, name='guardar_turnos'),
    path('management/shifts/list/', views.shift_list, name='shift_list'),
    path('management/leaves/add/', views.add_leave, name='add_leave'),
    path('management/leaves/list/', views.leave_list, name='leave_list'),
    path('management/report/', views.report_view, name='report_view'),
    path('api/get-shift-data/', views.get_shift_data, name='get_shift_data'),
]
