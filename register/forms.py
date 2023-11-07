from django import forms
from django.forms import ModelForm
from register.models import *


class RegiForm(forms.ModelForm):
    class meta:
        model= registration
        fields= ["_all_"]