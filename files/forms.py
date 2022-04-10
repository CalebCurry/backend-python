from django import forms
from django.forms import ModelForm
from .models import File

class UploadForm(ModelForm):
    class Meta:
        model = File
        fields = ['name', 'file', 'file_type']
        widgets = {
            'name': forms.TextInput(attrs={'placeholder': 'filename'})
        }