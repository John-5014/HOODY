from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from pyuploadcare.dj.models import ImageField

# Create your models here.




class Location(models.Model):
    locations = (
        ('Nairobi', 'Nairobi'),
        ('Kiambu', 'Kiambu'),
        ('Eastlands', 'Eastlands'),
        ('Machakos', 'Machakos'),
        ('Nakuru', 'Nakuru'),
        ('Thika', 'Thika'),

    )
    name = models.CharField(max_length=65, choices=locations)



    def save_loc(self):
        self.save()

    def delete_loc(self):
        self.delete()


    def __str__(self):
        return self.name



class Category(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name








