from django.db import models  
from django.forms import fields  
from .models import UploadScript, UploadImage 
from django import forms  
  
  
class UploadScriptForm(forms.ModelForm):  
    class Meta:  
        # To specify the model to be used to create form  
        model = UploadScript  
        # It includes all the fields of model  
        fields = '__all__' 

class UserImageForm(forms.ModelForm):  
    class Meta:  
        # To specify the model to be used to create form  
        model = UploadImage  
        # It includes all the fields of model  
        fields = ['image']