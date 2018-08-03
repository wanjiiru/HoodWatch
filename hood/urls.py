from django.conf.urls import url,include
from . import views



urlpatterns = [
        url(r'^$',views.home,name='home'),
        url(r'^business/view',views.display_business,name = 'viewbiz'),
        url(r'^business/',views.create_business,name = 'business'),
         url(r'^accounts/', include('registration.backends.simple.urls')),
         url(r'^profile/create/',views.create_profile,name = 'profile'),

]