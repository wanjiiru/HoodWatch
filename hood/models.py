from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.db import IntegrityError



# Create your models here.
class Neighbourhood(models.Model):
    name = models.CharField(max_length = 65)
    location = models.CharField(max_length = 65)
    occupants = models.PositiveIntegerField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


    def save_hood(self):
        self.save()

    def delete_hood(self):
        self.delete()

class Profile(models.Model):
    name = models.CharField(max_length = 65, blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    hood = models.ForeignKey(Neighbourhood, blank=True)
    bio = models.TextField(max_length=200)

    def __str__(self):
        return self.name


    def save_profile(self):
        self.save()

    def delete_profile(self):
        self.delete()

class Business(models.Model):
    name = models.CharField(max_length = 65)
    user = models.ForeignKey(User)
    hood = models.ForeignKey(Neighbourhood, on_delete=models.CASCADE)


    def __str__(self):
        return self.name


    def save_business(self):
        self.save()

    def delete_business(self):
        self.delete()


class Post(models.Model):

    user = models.ForeignKey(Profile, on_delete=models.CASCADE)
    post = models.TextField(max_length=300)
    hood = models.ForeignKey(Neighbourhood, on_delete=models.CASCADE)
    location = models.CharField(max_length = 65)
        
    def __str__(self):
        return self.post






