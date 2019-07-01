from django.shortcuts import render
from django.http import HttpResponse
from .models import artif_start

# Create your views here.
def homepage(request):
    return render(request = request, 
                     template_name='main/home.html',#"/home/linkgish/Desktop/WebApp2/ARTIF_project/ARTIF_project/templates/homepage/home.html", 
                     context={"artif_start":artif_start.objects.all})
    #return HttpResponse("Wow <strong>LinkGish</strong> is born today!!")
