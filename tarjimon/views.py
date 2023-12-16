from django.shortcuts import render
from django.http import HttpResponse
from .models import Lugat
# Create your views here.

def index(request):
     soz = request.GET.get('Q')
     if soz and soz != '':
        natija = Lugat.objects.filter(uzbekcha__contains = soz).all() | Lugat.objects.filter(inglizcha__contains = soz).all()
     else:
         return render(request, 'index.html',{})


     return render(request, 'index.html',{"natija" : natija})

 