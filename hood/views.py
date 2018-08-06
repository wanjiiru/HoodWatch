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





@login_required(login_url='/accounts/login/')
def display_profile(request, id):
    seekuser=User.objects.filter(id=id).first()
    profile = seekuser.profile
    profile_details = Profile.get_by_id(id)



    return render(request,'profile.html',locals())



def create_profile(request):
    current_user = request.user
    # profile = User.objects.get(username=current_user)
    if request.method == 'POST':
        form = ProfileForm(request.POST,request.FILES)
        if form.is_valid():
            profile=form.save(commit=False)
            profile.user = current_user
            profile.save()
            redirect('home')
    else:
        form = ProfileForm()
    return render(request,'new_profile.html', locals())

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
    this_hood = Neighbourhood.objects.all()
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.save()
            return redirect('index')
    else:
        form = PostForm()
    return render(request, 'newpost.html', locals())


@login_required(login_url='/accounts/login/')
def post(request):
    post = Post.get_post()
    return render(request,'post.html',locals())


@login_required(login_url='/accounts/login/')
def join(request, hoodId):
    '''
    This view function will implement adding
    '''
    neighbourhood = Neighbourhood.objects.get(pk=hoodId)
    if Join.objects.filter(user_id=request.user).exists():

        Join.objects.filter(user_id=request.user).update(hood_id=neighbourhood)
    else:

        Join(user_id=request.user, hood_id=neighbourhood).save()

    messages.success(request, 'Success! You have succesfully joined this Neighbourhood ')
    return redirect('home')






