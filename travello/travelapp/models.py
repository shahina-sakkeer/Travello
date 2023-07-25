from django.db import models

# Create your models here.

class Place(models.Model):
    name=models.CharField(max_length=200)
    image=models.ImageField(upload_to="pictures")
    description=models.CharField(max_length=200)


    def __str__(self):
        return self.name
    

class Team(models.Model):
    name=models.CharField(max_length=200) 
    about=models.CharField(max_length=200)
    image=models.ImageField(upload_to="pics")


    def __str__(self):
        return self.name   