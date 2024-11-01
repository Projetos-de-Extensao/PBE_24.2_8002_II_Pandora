from django.db import models

class Department(models.Model):
    name = models.CharField(max_length=100)

class Employee(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=254)  # Verifique se este campo está presente
    department = models.ForeignKey(Department, on_delete=models.CASCADE)

