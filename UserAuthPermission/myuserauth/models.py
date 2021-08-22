from django.db import models

# Create your models here.
class Students(models.Model):
    name = models.CharField(max_length=100)
    rollno = models.CharField(max_length=100)
    regdno = models.CharField(max_length=100)
    parrent = models.CharField(max_length=100)
    dob = models.DateField()
    address = models.CharField(max_length=300)
    image = models.ImageField(upload_to='pictures/', null=True, blank=True)
    document = models.FileField(upload_to='documents/', null=True, blank=True)

def __str__(self):
    return self.rollno