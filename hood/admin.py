from django.contrib import admin
from .models import Business, Neighbourhood,Profile,Post



# Register your models here.
admin.site.register(Business)
admin.site.register(Neighbourhood)
admin.site.register(Profile)
admin.site.register(Post)

