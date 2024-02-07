# en miapp/forms.py
from django import forms

class NombreForm(forms.Form):
    nombre = forms.CharField(label='Nombre')
