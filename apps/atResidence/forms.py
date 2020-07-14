from django import forms
from .models import *
from apps.base.models import *
from django.contrib.auth.models import User

class DocumentForm(forms.ModelForm):    
    zone = forms.CharField(
        widget = forms.TextInput(
            attrs = {'placeholder': 'Zone', 
                    'class': 'form-control', 
                    'list':'zones'}),
        label = 'Zone')
    residence_quarter = forms.CharField(
        widget = forms.TextInput(
            attrs = {'placeholder': 'Residence Quarter', 
                    'class': 'form-control',
                    'list':'quarters'}),
        label = 'Residence Quarter')



    first_witness = forms.CharField(
        widget = forms.TextInput(
            attrs = {'placeholder': 'witness', 
                    'class': 'form-control', 
                    'list':'witness'}),
        label = "Témoin 1 : ")

    second_witness = forms.CharField(
        widget = forms.TextInput(
            attrs = {'placeholder': 'witness', 
                    'class': 'form-control', 
                    'list':'witness'}),
        label = "Témoin 1 : ")

    quarter_leader = forms.CharField(
        widget = forms.TextInput(
            attrs = {'placeholder': 'witness', 
                    'class': 'form-control', 
                    'list':'witness'}),
        label = "Chef de Quartier : ")

    class Meta:
        model = Document
        fields = ("zone", "residence_quarter", "first_witness","second_witness","quarter_leader")

    def clean_zone(self, *arg,**kwargs):
        try:
            name = self.cleaned_data.get("zone")
            zone = Zone.objects.get(name=name)
            return zone
        except:
            raise forms.ValidationError("this zone is unknown")

    def clean_residence_quarter(self, *arg,**kwargs):
        try:
            name = self.cleaned_data.get("residence_quarter").split()[0]
            zone = self.cleaned_data.get("residence_quarter").split()[-1]
            quarter = Quarter.objects.get(name=name, zone__name=zone)
            return quarter
        except Exception as e:
            raise forms.ValidationError("this quarter is unknown")

    def clean_first_witness(self, *arg, **kwargs):
        try:
            first_name = self.cleaned_data.get("first_witness").split()[0]
            last_name = self.cleaned_data.get("first_witness").split()[-1]
            profile = User.objects.get(first_name=first_name, last_name=last_name)
            return profile
        except Exception as e:
            raise forms.ValidationError("unknown user")

    def clean_second_witness(self, *arg, **kwargs):
        try:
            first_name = self.cleaned_data.get("second_witness").split()[0]
            last_name = self.cleaned_data.get("second_witness").split()[-1]
            profile = User.objects.get(first_name=first_name, last_name=last_name)
            return profile
        except Exception as e:
            raise forms.ValidationError("unknown user")

    def clean_quarter_leader(self, *arg, **kwargs):
        try:
            first_name = self.cleaned_data.get("quarter_leader").split()[0]
            last_name = self.cleaned_data.get("quarter_leader").split()[-1]
            profile = User.objects.get(first_name=first_name, last_name=last_name)
            return profile
        except Exception as e:
            raise forms.ValidationError("unknown user")