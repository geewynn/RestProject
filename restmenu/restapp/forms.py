from .models import Restaurants, Menu
from django import forms


class addForm(forms.ModelForm):
    class Meta:
        model = Restaurants
        fields = '__all__'


class menuForm(forms.ModelForm):
    class Meta:
        model = Menu
        fields = '__all__'