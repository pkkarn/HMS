from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    roles_type = (('doctor','doctor'),('patient','patient'),('hr','hr'),('receptionist','receptionist'))
    role = models.CharField(default=1,choices=roles_type,max_length=15)


class Patient(models.Model):
    gender_choice = (
        ('male','male'),
        ('female','female'),
        ('others','others'),
    )
    blood_group = (
        ('A+','A+'),
        ('A-','A-'),
        ('AB-','AB-'),
        ('O-','O-'),
        ('O+','O+'),
    )
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    gender = models.CharField(default=1,choices=gender_choice,max_length=100)
    age = models.IntegerField()
    address = models.CharField(max_length=100)
    blood = models.CharField(default=1,choices=blood_group,max_length=100)
    med_reps = models.CharField(max_length=100)
    case_paper = models.CharField(max_length=100)
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.name

class Doctor(models.Model):
    gender_choice = (
        ('male','male'),
        ('female','female'),
        ('others','others'),
    )
    status_choice = (
        ('active','active'),
        ('non-active','non-active'),
    )
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    gender = models.CharField(default=1,choices=gender_choice,max_length=100)
    age = models.IntegerField()
    status = models.CharField(default=1,choices=status_choice,max_length=100)
    department = models.CharField(max_length=100)
    attendance = models.IntegerField()
    salary = models.IntegerField()

    def __str__(self):
        return self.name

class Appointments(models.Model):
    status_choice = (
        ('pending','pending'),
        ('completed','completed'),
    )
    date = models.DateField()
    time = models.CharField(max_length=30)
    doctor = models.ForeignKey(Doctor, null=True,on_delete=models.SET_NULL)
    patient = models.ForeignKey(Patient, null=True,on_delete=models.SET_NULL)
    status = models.CharField(default=1,choices=status_choice,max_length=100,null=True)
    def __str__(self):
        return self.patient.name


class Patient_Outstandings(models.Model):
    patient = models.ForeignKey(Patient, null=True, on_delete=models.SET_NULL)
    outstanding = models.IntegerField()
    paid = models.IntegerField()

    def __str__(self):
        return self.patient.name


class Doctor_Outstandings(models.Model):
    patient = models.ForeignKey(Patient, null=True, on_delete=models.SET_NULL)
    doctor = models.ForeignKey(Doctor, null=True, on_delete=models.SET_NULL)
    outstanding = models.IntegerField()
    paid = models.IntegerField()
    date = models.DateField()

    def __str__(self):
        return (self.patient.name+" Patient Of "+self.doctor.name)

class Prescription(models.Model):
    date = models.DateField()
    symptoms = models.CharField(max_length=100)
    description = models.TextField()
    patient = models.ForeignKey(Patient, null=True, on_delete=models.SET_NULL)
