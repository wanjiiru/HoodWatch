from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from .models import Post,Profile,Neighbourhood,Business
from django.db import transaction
from . forms import ProfileForm,BusinessForm,PostForm
from django.contrib.auth.models import User

# Create your views here.
@login_required(login_url = '/accounts/login')
def home(request):
    posts = Post.objects.all()
    businesses = Business.objects.all()
    hoods = Neighbourhood.objects.all()
    return render(request,'home.html',locals())



@transaction.atomic
def create_profile(request):
    current_user = request.user 
    if request.method == 'POST':
        form = ProfileForm(request.POST,instance=request.user)
        if form.is_valid():
            form.save()
            return redirect( home )
    else:
        form = ProfileForm()
    return render(request,'profile.html', locals())

def create_business(request):
    current_user = request.user
    # owner = Profile.get_by_id(current_user)
    # hood = Neighbourhood.objects.all()
    if request.method == 'POST':
        form = BusinessForm(request.POST,request.FILES)
        if form.is_valid():
            new_biz=form.save(commit = False)
            new_biz.owner = current_user
            # new_biz.hood =hood
            new_biz.save
            return redirect(home)
    else:
        form = BusinessForm()
    return render(request,"businessform.html",locals())


def display_business(request):
    user = request.user
    owner = Profile.get_by_id(user)
    businesses = Business.objects.all()


    return render (request, 'business.html', locals())




