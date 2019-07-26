# from django.shortcuts import render
# from django.http import HttpResponse
# from .models import artif_start

# New tutorial
from main.models import UserProfileInfo
from django.shortcuts import render
from main.forms import UserForm,UserProfileInfoForm # how?
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.contrib.auth.decorators import login_required
###

# Create your views here.
def homepage(request):
    return render(request = request, 
                     template_name='main/index.html',#"/home/linkgish/Desktop/WebApp2/ARTIF_project/ARTIF_project/templates/homepage/home.html", 
                     #context={"artif_start":artif_start.objects.all}
                     )
    #return HttpResponse("Wow <strong>LinkGish</strong> is born today!!")

def appsPage(request):
    return render(request= request,
                    template_name='main/apps.html')

def loginPage(request):
    return render(request= request,
                    template_name='main/login.html')

# def registerPage(request):
#     return render(request= request,
                    # template_name='main/register.html')

# New tutorial
# def index(request):
#     return render(request,'dappx/index.html')@login_required
def special(request):
    return HttpResponse("You are logged in !")
# @login_required
def logoutPage(request):
    logout(request)
    # return HttpResponseRedirect(reverse('index'))
    return HttpResponseRedirect('/')# reverse('main/apps.html'))

def registerPage(request):
    registered = False
    if request.method == 'POST':
        user_form = UserForm(data=request.POST)
        profile_form = UserProfileInfoForm(data=request.POST)
        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.save()
            profile = profile_form.save(commit=False)
            profile.user = user
            if 'profile_pic' in request.FILES:
                print('found it')
                profile.profile_pic = request.FILES['profile_pic']
            profile.save()
            registered = True
            return HttpResponseRedirect('masuk')#reverse(''))# ('index'))
        else:
            print(user_form.errors,profile_form.errors)
    else:
        user_form = UserForm()
        profile_form = UserProfileInfoForm()
    return render(request,
                        template_name= 'main/register.html', # 'dappx/registration.html',
                        context={'user_form':user_form, 'profile_form':profile_form, 'registered':registered})

def isCorrect(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user:
            if user.is_active:
                login(request,user)
                return HttpResponseRedirect('/')#reverse(''))# ('index'))
            else:
                return HttpResponse("Your account was inactive.")
        else:
            print("Someone tried to login and failed.")
            print("They used username: {} and password: {}".format(username,password))
            return HttpResponse("Invalid login details given.")
    else:
        return render(request, 
                    #'dappx/login.html', {})
                    template_name='main/login.html', 
                    context= {})
###