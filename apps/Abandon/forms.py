from django import forms
from datetime import date
from .models import *
from apps.base.models import *

class DocumentForm(forms.ModelForm):
    objet_abandon     = forms.CharField(label="objet abandone", max_length=100, widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'objet abandonne '}))
    tuteurAcueillantObjetAbandon      = forms.CharField(label="Tutilleur", max_length=100, widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'tuteur acueillant l\'bjet abandonne '}))

    zone = forms.ModelChoiceField(
        widget = forms.Select(
            attrs = {'placeholder': 'Zone', 'class': 'form-control', 'id':'zones'}),
        label = 'Zone',
        queryset = Zone.objects.all())
    
    residence_quarter = forms.ModelChoiceField(
        widget = forms.Select(
            attrs = {'placeholder': 'Residence Quarter', 'class': 'form-control','id':'quarters'}),
        label = 'Residence Quarter',
        queryset = Quarter.objects.all())

    
    date_delivrated = forms.DateField(
        widget=forms.SelectDateWidget(
            years=range(1990, date.today().year + 1),
            attrs={'placeholder':'yyyy-mm-dd ', 'class':'form-control',
                'style':'width: auto;display: inline-block;'}),
        label='date')

    class Meta:
        model = Document
        fields = ("zone", "residence_quarter", "objet_abandon", 'date_delivrated',"tuteurAcueillantObjetAbandon")

    