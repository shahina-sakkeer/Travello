from django.shortcuts import render
from . models import Place,Team

# Create your views here.

def demo(request):
    obj=Place.objects.all()
    return render(request,"index.html",{"result":obj})

def team(request):
    res=Team.objects.all()
    return render(request,"index.html",{"value":res})
    
