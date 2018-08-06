from django.conf.urls import url,include
from . import views



urlpatterns = [
        url(r'^$',views.home,name='home'),
        url(r'^hoods', views.all_hoods, name='hoods'),
        url(r'^business/view',views.display_business,name = 'viewbiz'),
        url(r'^business/',views.create_business,name = 'business'),
        url(r'^accounts/', include('registration.backends.simple.urls')),
        url(r'^profile/create/',views.create_profile,name = 'profile'),
        url(r'^showprofile/(?P<id>\d+)', views.display_profile, name='showprofile'),
        url(r'^new/post$', views.new_post, name='newpost'),
        url(r'^join/(\d+)', views.join, name='joinHood'),
        url(r'^createHood/$', views.createHood, name='createHood'),
        url(r'^comment/(?P<post_id>\d+)', views.comment, name='comment'),

]