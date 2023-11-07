from django.shortcuts import render
from django.http import HttpResponse
from .models import *
from .forms import *
# Create your views here.

def index(request):
    context={}
    form=RegiForm()
    ID=registration.objects()
    context['ID']=ID
    context['title']='home'
    context['form']=form
    return render(request, 'index.html',context)
