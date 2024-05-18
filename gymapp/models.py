from django.contrib.auth.models import AbstractUser
from django.db import models
from django.db.models import DO_NOTHING


# Create your models here.
class Login(AbstractUser):
    is_staff = models.BooleanField(default=False)
    is_instructor = models.BooleanField(default=False)
    is_physician = models.BooleanField(default=False)
    is_customer = models.BooleanField(default=False)


class Instructor(models.Model):
    user = models.ForeignKey(Login, on_delete=models.CASCADE)
    Instructor_Id = models.IntegerField()
    Instructor_Name = models.CharField(max_length=30)
    Email = models.EmailField()
    Contact_Number = models.CharField(max_length=10)


    def __str__(self):
        return self.Instructor_Name


class Physician(models.Model):
    user1 = models.ForeignKey(Login, on_delete=models.CASCADE)
    Physician_Id = models.IntegerField()
    Physician_Name = models.CharField(max_length=30)
    Physician_Email = models.EmailField()
    Physician_Number = models.CharField(max_length=10)


class Customer(models.Model):
    user2 = models.ForeignKey(Login, on_delete=models.CASCADE)
    Customer_Id = models.IntegerField()
    Customer_Name = models.CharField(max_length=30)
    Customer_Age = models.IntegerField()
    Customer_Email = models.EmailField()
    Customer_Number = models.CharField(max_length=10)

    # class Equipments(models.Model):
    #     equipments_name = models.CharField(max_length=50)
    #     image = models.FileField(upload_to='images/')
    #

    def __str__(self):
        return self.Customer_Name


# class FirstAid(models.Model):
#
#     name= models.CharField(max_length=30)
#
#     image = models.ImageField(upload_to='images/')
#
#     def __str__(self):
#         return self.name

class CustMembership(models.Model):
    name = models.CharField(max_length=30)
    email = models.EmailField()
    contact_number = models.CharField(max_length=10)


class CustomerDoubts(models.Model):
    user4 = models.ForeignKey(Login, on_delete=DO_NOTHING)
    date = models.DateField(auto_now=True)
    doubts = models.TextField()
    reply = models.TextField(blank=True, null=True)


class CustomerComplaint(models.Model):
    user5 = models.ForeignKey(Login, on_delete=DO_NOTHING)
    date = models.DateField(auto_now=True)
    complaints = models.TextField()
    reply = models.TextField(blank=True, null=True)


class GymServices(models.Model):
    name = models.CharField(max_length=30)
    image = models.ImageField(upload_to='images/')
    description = models.TextField()








class Membership(models.Model):
    membership_name = models.CharField(max_length=50)
    duration = models.CharField(max_length=100)
    image = models.FileField(upload_to='images/')

    def __str__(self):
        return self.membership_name




class Membershipjoin(models.Model):
    user = models.ForeignKey(Customer, on_delete=models.CASCADE)
    schedule = models.ForeignKey(Membership, on_delete=models.CASCADE)
    status = models.IntegerField(default=0)

class Idietadd(models.Model):
    user=models.ForeignKey(Customer,on_delete=models.CASCADE)
    breakfast=models.TextField()
    lunch=models.TextField()
    dinner=models.TextField()


class HealthDetails(models.Model):

    sex_choices = choices = (
        ('MALE' , 'male'),
        ('FEMALE' , 'female')
    )
    user = models.ForeignKey(Customer, on_delete=models.CASCADE)
    age = models.IntegerField()
    sex  = models.CharField(max_length=100,choices=sex_choices)
    height = models.IntegerField()
    weight = models.IntegerField()

class Fee(models.Model):

      customer_name=models.CharField(max_length=100)
      duration=models.CharField(max_length=100)
      fee_amount=models.CharField(max_length=100)

