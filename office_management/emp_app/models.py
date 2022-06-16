from django.db import models

# Create your models here.
class Department(models.Model):
    name = models.CharField(max_length=200, unique=True)
    location = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Role(models.Model):
    name = models.CharField(max_length=100, null=False)

    def __str__(self):
        return self.name

class Employee(models.Model):
    first_name = models.CharField(max_length=100, null=False)
    last_name = models.CharField(max_length=100)
    dept = models.ForeignKey(Department, on_delete=models.CASCADE)
    salary = models.IntegerField(default=0)
    address = models.CharField(max_length=300)
    city = models.CharField(max_length=100)
    role = models.ForeignKey(Role, on_delete=models.CASCADE)
    phone = models.IntegerField(default=0)
    hire_date = models.DateField()


    def __str__(self):
        return "%s %s %s" %(self.first_name, self.last_name, self.phone)