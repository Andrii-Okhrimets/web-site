from django import forms
from django.forms import ModelForm
from .models import Reviews

class ReviewsForm(forms.ModelForm):
    class Meta:
        model = Reviews
        fields = ('name', 'taxt', 'email')
