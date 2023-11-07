from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import *
from .forms import *
# Create your views here.

def studentfees(request):
    Fees= feeBalance.objects.all().values
    template= loader.get_template('fees.html')
    context= {
        'Fee balance': Fees
    }
    return HttpResponse(template.render(context,request))
    
