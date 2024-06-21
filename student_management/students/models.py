from django.db import models

class Student(models.Model):
    name = models.CharField(max_length=100)  
    age = models.PositiveIntegerField()      
    email = models.EmailField(unique=True)  
    phone = models.CharField(max_length=15)  
    location = models.CharField(max_length=100)  
    hobby = models.CharField(max_length=100)     

    def __str__(self):
        return self.name
