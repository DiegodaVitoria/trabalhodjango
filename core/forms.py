# -*- coding:utf-8 -*-

from django import forms
from .models import *

class ClienteForm(forms.ModelForm):
    class Meta:
        model = Usuario
        fields = ["nome", "email", "passkey"]

