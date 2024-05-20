from django import forms
from .models import NewCars
from tataapp.models import FeaturedCars

class Update_Newcars(forms.ModelForm):
    class Meta:
        model = NewCars
        fields = ['name', 'desc', 'price', 'image']


class Update_FeaturedCars(forms.ModelForm):
    class Meta:
        model = FeaturedCars
        fields = ['name', 'desc', 'price', 'image']
