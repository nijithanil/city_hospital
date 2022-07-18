from django.db import models


# Create your models here.

class Department(models.Model):
    objects = None
    dep_name = models.CharField(max_length=100)
    dep_description = models.TextField()

    def __str__(self):
        return self.dep_name


class Doctor(models.Model):
    doc_name = models.CharField(max_length=250)
    doc_spec = models.CharField(max_length=250)
    dep_name = models.ForeignKey(Department, on_delete=models.CASCADE)
    doc_img = models.ImageField(upload_to='doctors_img')

    def __str__(self):
        # concatenate the doc name and doc spec
        return 'Dr ' + self.doc_name + ' - (' + self.doc_spec + ')'


class Booking(models.Model):
    p_name = models.CharField(max_length=250)
    p_phone = models.CharField(max_length=10)
    p_email = models.EmailField()
    doc_name = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    booking_date = models.DateField()
    booked_on = models.DateField(auto_now=True)


