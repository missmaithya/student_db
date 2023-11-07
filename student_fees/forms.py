from django import forms
from django.forms import ModelForm
from .models import *


class fee_Form(forms.ModelForm):
    class meta:
        model= feePayments
        fields= ["_all_"]

class Balance_Form(forms.ModelForm):
    class meta:
        model= feeBalance
        fields= ["_all_"]