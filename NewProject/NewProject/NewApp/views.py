from django.shortcuts import render
from django.http import HttpResponse
from .models import Place
from .models import Team

# Create your views here.
def newapplication(request):
    obj = Place.objects.all()
    t = Team.objects.all()
    return render(request, "index.html", {'result':obj,'team': t})


