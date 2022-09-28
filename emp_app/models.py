from django.db import models


# Create your models here.
class Department(models.Model):
    name = models.CharField(max_length=100, null=False)
    location = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Role(models.Model):
    name = models.CharField(max_length=100, null=False)

    def __str__(self):
        return self.name

class Employee(models.Model):
    first_name= models.CharField(max_length=100, null=False)
    last_name = models.CharField(max_length=100, null=False)
    dept = models.ForeignKey(Department, on_delete=models.CASCADE)
    salary = models.IntegerField(default=0)
    bonus = models.IntegerField(default=0)
    role =  models.ForeignKey(Role, on_delete=models.CASCADE)
    phone = models.IntegerField(default=0)


    def __str__(self):
        return "%s %s %s" %(self.first_name, self.last_name, self.phone)

# user table
class Customer(models.Model):
    first_name = models.CharField(max_length=100, null=False)
    last_name = models.CharField(max_length=100, null=False)
    phone = models.IntegerField(default=0)
    e_mail = models.EmailField(max_length=100, null=False)
    password = models.CharField(max_length=100,null=False)

    def get_customer_by_email(e_mail):
        try:
            return Customer.objects.get(e_mail=e_mail)
        except:
            return False
