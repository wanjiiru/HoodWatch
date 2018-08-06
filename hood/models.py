from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.db import IntegrityError
from django.dispatch import receiver




# Create your models here.
class Neighbourhood(models.Model):
    name = models.CharField(max_length = 65)
    locations = (
        ('Nairobi', 'Nairobi'),
        ('Zurich', 'Zurich'),
        ('Paris', 'Paris'),
        ('Munich', 'Munich'),
        ('Tokyo', 'Tokyo'),
        ('London', 'London'),
        ('Melbourne', 'Melbourne'),
        ('Sydney', 'Sydney'),
        ('Berlin', 'Berlin')
    )
    loc  = models.CharField(max_length=65, choices=locations)
    occupants = models.PositiveIntegerField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural = 'Location'



    def __str__(self):
        return f"{self.loc}"


    def save_hood(self):
        self.save()

    def delete_hood(self):
        self.delete()

class Profile(models.Model):
    name = models.CharField(max_length = 65, blank=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    hood = models.ForeignKey(Neighbourhood, blank=True, null=True)
    bio = models.TextField(max_length=200)

    def __str__(self):
        return self.name


    def save_profile(self):
        self.save()

    def delete_profile(self):
        self.delete()

    @receiver(post_save, sender=User)
    def create_user_profile(sender, instance, created, **kwargs):
        if created:
            Profile.objects.create(user=instance)
    #
    # @receiver(post_save, sender=User)
    # def save_user_profile(sender, instance, **kwargs):
    #     instance.profile.save()

    
    @classmethod
    def get_by_id(cls,id):
        profile = cls.objects.get(user = id)
        return profile

class Business(models.Model):
    name = models.CharField(max_length = 65)
    user = models.ForeignKey(User)
    hood = models.ForeignKey(Neighbourhood,blank=True)
    email = models.CharField(max_length=100)


    def __str__(self):
        return self.name


    def save_business(self):
        self.save()

    def delete_business(self):
        self.delete()


class Post(models.Model):

    user = models.ForeignKey(Profile, on_delete=models.CASCADE)
    post = models.TextField(max_length=300)
    hood = models.ForeignKey(Neighbourhood, blank=True,on_delete=models.CASCADE)
    location = models.CharField(max_length = 65)
        
    def __str__(self):
        return self.post






