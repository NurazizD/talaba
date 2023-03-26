from django.shortcuts import render
from django.views.generic import ListView,CreateView
from .models import Pupil
from django.db.models import Q
from django.urls import reverse
# Create your views here.
class Puple_new(CreateView):
    model = Pupil
    fields = ['ism','yosh','tugulgan_kun','guruh','tel_raqam']
    template_name = 'new.html'

def Puple_view(request):
    if 'q' in request.GET:
        q = request.GET.get('q')
        pupil = Pupil.objects.filter(Q(ism__icontains=q))
        
    else:
        pupil = Pupil.objects.all()
    return render(request,'list.html',{"pupil":pupil})
    
def home(request):
    return render(request,'home.html')