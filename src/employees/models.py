from django.db import models

from bases.model import BaseModel

# Create your models here.

class EmployeePosition(BaseModel):
    name = models.CharField(max_length=100)
    duties = models.TextField(blank=True, null=True)

    class Meta:
        verbose_name = 'Employee Position'
        verbose_name_plural = 'Employee Positions'
        db_table = 'employee_positions'

class Employee(BaseModel):
    user = models.ForeignKey('users.User', on_delete=models.CASCADE)
    position = models.ForeignKey(EmployeePosition, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Employee'
        verbose_name_plural = 'Employees'
        db_table = 'employees'