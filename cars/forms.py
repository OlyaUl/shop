from django import forms
from .models import Car, CarModel, Color, Specifications, Image


class CarForm(forms.ModelForm):
    # name = forms.CharField(help_text="this is name")
    # name = forms.CharField(max_length=10)

    class Meta:
        model = Car
        fields = '__all__'
