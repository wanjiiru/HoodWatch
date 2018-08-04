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



def create_profile(request):
    profile = User.objects.get(username=request.user)
    if request.method == 'POST':
        form = ProfileForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return redirect( home )
    else:
        form = ProfileForm()
    return render(request,'profile.html', locals())

def create_business(request):
    current_user = request.user
    print(Profile.objects.all())
    owner = Profile.get_by_id(current_user)
    # this_hood = Neighbourhood.objects.all()
    if request.method == 'POST':
        form = BusinessForm(request.POST,request.FILES)
        if form.is_valid():
            new_biz=form.save(commit=False)
            new_biz.user = current_user
            # new_biz.hood =this_hood
            new_biz.save()
            return redirect(home)
    else:
        form = BusinessForm()
    return render(request,"businessform.html",locals())


def display_business(request):
    user = request.user
    owner = Profile.get_by_id(user)
    businesses = Business.objects.all()


    return render (request, 'business.html', locals())


@login_required(login_url='/accounts/login/')
def new_post(request):

    current_user = request.user
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.save()
            return redirect('index')
    else:
        form = PostForm()
    return render(request, 'new_post.html', {"form": form})


@login_required(login_url='/accounts/login/')
def post(request):
    post = Post.get_post()
    return render(request,'post.html',{'post':post})

def leave_hood(request):
    current_user = request.user
    if request.method == 'POST':
        form = HoodForm(request.POST )
        if form.is_valid():
            neighborhoods = Neighborhood()
            hood=form.save(commit=False)
            hood.save()
            return render(request,'leave.html',{"form": form})




