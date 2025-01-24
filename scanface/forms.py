from django import forms
from .models import Scanface
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
class Valueform(forms.ModelForm):
 #   Rasi = forms.ChoiceField(choices = Rasi_CHOICES)
    class Meta:
        model = Scanface
        fields = "__all__"