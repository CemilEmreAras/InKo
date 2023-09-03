from django.shortcuts import render
from .models import *
# Create your views here.

def index(request):
    eğitimler=Eğitimler.objects.all()
    kadrolar=Kadro.objects.all()
    context={
        "eğitimler":eğitimler,
        "kadrolar":kadrolar
    }


    return render(request,"index.html",context)