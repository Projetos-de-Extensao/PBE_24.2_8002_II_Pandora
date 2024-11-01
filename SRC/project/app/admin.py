from django.contrib import admin
from .models import Employee, Department

class EmployeeInline(admin.TabularInline):
    model = Employee
    extra = 0  # Número de campos extras a serem exibidos para novos empregados

class DepartmentAdmin(admin.ModelAdmin):
    inlines = [EmployeeInline]

admin.site.register(Department, DepartmentAdmin)
admin.site.register(Employee)
