from django.db import models

# Create your models here.


class Doctor(models.Model):
    name =models.CharField(max_length=45)
    mobile =models.IntegerField()
    special =models.CharField(max_length=45)

    def __str__(self) :
        return self.name


class Patient(models.Model):
    name=models.CharField(max_length=45)
    mobile=models.IntegerField(null =True)
    gender=models.CharField(max_length=10)
    addresh=models.CharField(max_length=150)

    def __str__(self) :
        return self.name

   

    
class Appointment(models.Model):
    doctor=models.ForeignKey(Doctor,on_delete=models.CASCADE)
    patient=models.ForeignKey(Patient,on_delete=models.CASCADE)
    mobile=models.IntegerField(null =True)
    date1 =models.IntegerField()
    time1=models.DateField()
    

    def __str__(self) :
        return self.doctor.name+"__"+self.patient.name




