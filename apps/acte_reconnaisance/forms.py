from django import forms
from .models import *
from apps.base.models import *

class DocumentForm(forms.ModelForm):
    zone = forms.ModelChoiceField(
        widget = forms.Select(
            attrs = {'placeholder': 'Zone', 
                    'class': 'form-control', 
                    'id':'zone'}),
        label='Zone',
        queryset = Zone.objects.all())
    
    residence_quarter = forms.ModelChoiceField(
        widget = forms.Select(
            attrs = {'placeholder': 'Residence Quarter', 
                    'class': 'form-control',
                    'id':'residence_quarter'}),
        label='Residence Quarter',
        queryset = Quarter.objects.all())
        
    volume = forms.CharField(
        widget = forms.TextInput(
            attrs = {'placeholder': 'Volume', 
                    'class': 'form-control'}),
        label = 'Volume')
        
    acte = forms.CharField(
        widget = forms.TextInput(
            attrs = {'placeholder': 'Acte', 
                    'class': 'form-control'}),
        label = 'Acte')
	
    witness1 = forms.CharField(
        widget = forms.TextInput(
            attrs = {'placeholder': 'Witness 1', 
                    'class': 'form-control'}),
        label = 'Witness 1')

    witness2 = forms.CharField(
        widget = forms.TextInput(
            attrs = {'placeholder': 'Witness 2', 
                    'class': 'form-control'}),
        label = 'Witness 2')

    years_letter = forms.CharField(
        widget = forms.TextInput(
            attrs = {'placeholder': 'Year', 
                    'class': 'form-control'}),
        label = 'Year')

    days_letter = forms.CharField(
        widget = forms.TextInput(
            attrs = {'placeholder': 'Day', 
                    'class': 'form-control'}),
        label = 'Day')

    months_letter = forms.CharField(
        widget = forms.TextInput(
            attrs = {'placeholder': 'Month', 
                    'class': 'form-control'}),
        label = 'Month')
        
    wife = forms.CharField(
        widget = forms.TextInput(
            attrs = {'placeholder': 'Wife', 
                    'class': 'form-control'}),
        label = 'Wife')
        
    work = forms.CharField(
        widget = forms.TextInput(
            attrs = {'placeholder': 'Work', 
                    'class': 'form-control'}),
        label = 'Work')
        
    witness_work1 = forms.CharField(
        widget = forms.TextInput(
            attrs = {'placeholder': 'Witness Work 1', 
                    'class': 'form-control'}),
        label = 'Witness Work 1')
        
    witness_work2 = forms.CharField(
        widget = forms.TextInput(
            attrs = {'placeholder': 'Witness Work 2', 
                    'class': 'form-control'}),
        label = 'Witness Work 2')

    witness_province1 = forms.ModelChoiceField(
        widget = forms.Select(
            attrs={'placeholder': 'Witness province 1',
                    'id':'witness_province1', 
                    'class': 'form-control'}),
        label = 'Witness province 1',
        queryset = Province.objects.all())

    witness_province2 = forms.ModelChoiceField(
        widget = forms.Select(
            attrs={'placeholder': 'Witness province 2',
                    'id':'witness_province2', 
                    'class': 'form-control'}),
        label = 'Witness province 2',
        queryset = Province.objects.all())

    witness_age1 = forms.CharField(
        widget = forms.TextInput(
            attrs = {'placeholder': 'Witness age 1', 
                    'class': 'form-control'}),
        label = 'Witness age 1')

    witness_age2 = forms.CharField(
        widget = forms.TextInput(
            attrs = {'placeholder': 'Witness age 2', 
                    'class': 'form-control'}),
        label = 'Witness age 2')

    child = forms.CharField(
        widget = forms.TextInput(
            attrs = {'placeholder': 'Child name', 
                    'class': 'form-control'}),
        label = 'Child name')

    child_day = forms.CharField(
        widget = forms.TextInput(
            attrs = {'placeholder': 'Child day', 
                    'class': 'form-control'}),
        label = 'Child day')

    child_month = forms.CharField(
        widget = forms.TextInput(
            attrs = {'placeholder': 'Child month', 
                    'class': 'form-control'}),
        label = 'Child month')

    child_year = forms.CharField(
        widget = forms.TextInput(
            attrs = {'placeholder': 'Child year', 
                    'class': 'form-control'}),
        label = 'Child year')

    wife_age = forms.CharField(
        widget = forms.TextInput(
            attrs = {'placeholder': 'Wife age', 
                    'class': 'form-control'}),
        label = 'Wife age')

    wife_work = forms.CharField(
        widget = forms.TextInput(
            attrs = {'placeholder': 'Wife work', 
                    'class': 'form-control'}),
        label = 'Wife work')

    wife_province = forms.ModelChoiceField(
        widget = forms.Select(
            attrs = {'placeholder': 'Wife province',
                    'id':'wife_province',
                    'class': 'form-control'}),
        label='Wife province',
        queryset = Province.objects.all())


    class Meta:
        model = Document
        fields = ("residence_quarter", "zone", "volume", "acte", "years_letter", "days_letter",
        "months_letter", "work", "witness1", "witness2", "witness_work1", "witness_work2",
        "witness_age1", "witness_age2", "witness_province1", "witness_province2", "child", "child_day",
        "child_month", "child_year", "wife_age", "wife_work", "wife_province", "wife",  )
