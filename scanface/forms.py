from django import forms
from .models import FaceLogin
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
class Valueform(forms.ModelForm):
 #   Rasi = forms.ChoiceField(choices = Rasi_CHOICES)
    class Meta:
        model = FaceLogin
        fields = ['verified', 'distance', 'threshold', 'model', 'detector_backend', 'similarity_metric', 'facial_areas', 'time']
        widgets = {
            'verified': forms.TextInput(attrs={'class': 'form-control'}),
            'distance': forms.TextInput(attrs={'class': 'form-control'}),
            'threshold': forms.TextInput(attrs={'class': 'form-control'}),
            'model': forms.TextInput(attrs={'class': 'form-control'}),
            'detector_backend': forms.TextInput(attrs={'class': 'form-control'}),
            'similarity_metric': forms.TextInput(attrs={'class': 'form-control'}),
            'facial_areas': forms.TextInput(attrs={'class': 'form-control'}),
            'time': forms.TextInput(attrs={'class': 'form-control'})
        }