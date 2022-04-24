from django.db import models
from django import forms
from  .models import Complaint, Contact
from django.contrib.auth.forms import UserCreationForm


class ComplaintForm(forms.ModelForm):
    class Meta:
        model= Complaint
        fields = ('name','enrollment','regarding','department','mobile','email','image','detail')
    
class ContactUs(forms.ModelForm):
    class Meta:
        model= Contact
        fields = ('name','department','mobile','email','reason')

