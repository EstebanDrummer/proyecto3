#encoding:utf-8
from django.forms import ModelForm
from django import forms
from django.forms.extras.widgets import SelectDateWidget

TOPIC_CHOICES = (
    ('PAD', 'Colombia peso A USA Dolar'),
    ('DAP', 'Dolar USA a Colombia peso'),
)

class ContactoForm(forms.Form):
	#correo = forms.EmailField(label='Tu correo electrónico')
	valor = forms.CharField(widget=forms.TextInput)

class SeleccionForm(forms.Form):
	Monedas = forms.ChoiceField(choices =TOPIC_CHOICES)

class ValorForm(forms.Form):
	#correo = forms.EmailField(label='Tu correo electrónico')
	valor = forms.CharField(widget=forms.TextInput)
	#contenido1=forms.CharField(widget=forms.TextInput)