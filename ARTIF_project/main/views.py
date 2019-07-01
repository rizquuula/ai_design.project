from django.shortcuts import render
from django.http import HttpResponse
from .models import artif_start

# Create your views here.
def homepage(request):
    # return render(request = request, 
    #                 template_name="homepage/home.html", 
    #                 context={"Start_app":artif_start.objects.all})
    return HttpResponse("Wow <strong>LinkGish</strong> is born today!!")
