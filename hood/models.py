from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.db import IntegrityError



# Create your models here.
class Neighbourhood(models.Model):
    name = models.CharField(max_lenghth = 65)
    location = models.CharField(max_length = 65)
    occupants = models.PositiveIntegerField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


    def save_hood(self):
        self.save()

    def delete_hood(self):
        self.delete()



        
