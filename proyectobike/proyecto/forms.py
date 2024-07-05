from django import forms
from .models import Arriendo

class ArriendoForm(forms.ModelForm):
    class Meta:
        model = Arriendo
        fields = ['bike_model', 'start_date', 'end_date', 'price']
