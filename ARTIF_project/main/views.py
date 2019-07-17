from django.shortcuts import render
from django.http import HttpResponse
from .models import artif_start

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

def registerPage(request):
    return render(request= request,
                    template_name='main/register.html')
