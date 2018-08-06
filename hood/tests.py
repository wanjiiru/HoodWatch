from django.test import TestCase
from .models import Neighbourhood,Business,User,Post,Comments
from django.contrib.auth.models import User


# Create your tests here.
class NeighborhoodTestClass(TestCase):
    def setUp(self):
        self.new_user = User(username='nish',email='nish@gmail.com')
        self.new_user.save()
        self.thome = Neighbourhood(name='nyati',location='thome',occupants=5)
        self.thome.save()

    def tearDown(self):
        User.objects.all().delete()
        Neighbourhood.objects.all().delete()

    def test_instance(self):
        self.assertTrue(isinstance(self.thome,Neighbourhood))

    def test_save_neighborhood(self):
        self.thome.save_neighborhood()
        neighborhood = Neighbourhood.objects.all()
        self.assertTrue(len(neighborhood)>0)




class BusinessTestClass(TestCase):
    def setUp(self):
        self.new_user=User(username="liz",email="liz@gmail.com")
        self.new_user.save()
        self.thome = Neighbourhood(name='nyati',location='thome',occupants_count=5,admin=self.new_user)
        self.thome.save_neighborhood()
        self.kinyozi = Business(name='kinyozi',email='liz@gmail.com',user=self.new_user,neighborhood=self.thome)
        self.kinyozi.save()

    def tearDown(self):
        User.objects.all().delete()
        Neighbourhood.objects.all().delete()
        Business.objects.all().delete()

    def test_instance(self):
        self.assertTrue(isinstance(self.kinyozi,Business))

    def test_save_business(self):
        self.kinyozi.save_business()
        business =  Business.objects.all()
        self.assertTrue(len(business)>0)




class PostTestClass(TestCase):
    def setUp(self):
        self.new_user=User(username="liz",email="liz@gmail.com")
        self.new_user.save()
        self.thome = Neighbourhood(name='nyati',location='thome',occupants_count=5,admin=self.new_user)
        self.thome.save_neighborhood()
        self.nish = User(name="liz",user=self.new_user,neighborhood=self.thome)
        self.nish.save_user()
        self.new_post=Post(post='Test dfghj post',author=self.liz)

    def tearDown(self):
        User.objects.all().delete()
        Neighbourhood.objects.all().delete()
        User.objects.all().delete()
        Post.objects.all().delete()

    def test_instance(self):
        self.assertTrue(isinstance(self.new_post,Post))

    def test_save_post(self):
        self.new_post.save_post()
        post =  Post.objects.all()
        self.assertTrue(len(post)>0)




class UserTestClass(TestCase):
    def setUp(self):
        self.new_user=User(username="liz",email="liz@gmail.com")
        self.new_user.save()
        self.thome = Neighbourhood(name='nyati',location='thome',occupants_count=5,admin=self.new_user)
        self.thome.save_neighborhood()
        self.nish = User(name="lizziw",user=self.new_user,neighborhood=self.thome)
        self.nish.save()

    def tearDown(self):
        User.objects.all().delete()
        Neighbourhood.objects.all().delete()
        User.objects.all().delete()

    def test_instance(self):
        self.assertTrue(isinstance(self.liz,User))
