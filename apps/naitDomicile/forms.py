from django import forms
from .models import *
from apps.base.models import *
from datetime import date

class DocumentForm(forms.ModelForm):

    zone = forms.ModelChoiceField(
        widget = forms.Select(
            attrs = {'placeholder': 'Zone', 
                    'class': 'form-control', 
                    'list':'zones'}),
        label = 'Zone de residence actuelle',
        queryset = Zone.objects.all())

    residence_quarter = forms.ModelChoiceField(
        widget = forms.Select(
            attrs = {'placeholder': 'Residence Quarter', 
                    'class': 'form-control',
                    'list':'quarters'}),
        label = 'Quartier de residence actuelle',
        queryset = Quarter.objects.all())

    child_name =  forms.CharField(
        widget = forms.TextInput(
            attrs = {'placeholder': "Nom Enfant", 
                    'class': 'form-control',}),
        label = "Nom complet de l'enfant")

    child_birth = forms.DateField(widget=forms.TextInput(
            attrs={'placeholder':'date delivrated ', 'type':'date',
                'class':'form-control',}),
        label='Date de naissance enfant :', required=False,initial=date.today())

    child_birth_quarter = forms.ModelChoiceField(
        widget = forms.TextInput(
            attrs = {'placeholder': 'Quartier naissance', 
                    'class': 'form-control', 
                    'list':'quarters'}),
        label = "Quartier de naissance de l'enfant",
        queryset = Quarter.objects.all())

    child_mother = forms.ModelChoiceField(
        widget = forms.Select(
            attrs = {'placeholder': 'Mère', 
                    'class': 'form-control', 
                    'list':'profiles'}),
        label = "Mère de l'enafant",
        queryset = Profile.objects.all())

    first_witness = forms.ModelChoiceField(
        widget = forms.Select(
            attrs = {'placeholder': 'Témoin 1', 
                    'class': 'form-control', 
                    'list':'profiles'}),
        label = "Temoins 1 : ",
        queryset = Profile.objects.all())

    second_witness = forms.ModelChoiceField(
        widget = forms.Select(
            attrs = {'placeholder': 'Temoin 2', 
                    'class': 'form-control', 
                    'list':'profiles'}),
        label = "Témoin 2 : ",
        queryset = Profile.objects.all())

    class Meta:
        model = Document
        # fields = ("zone_leader", "zone", "beneficiary", "father", "mother", "birth_quarter", "birth_year", "birth_commune", "birth_province", "nationality", "etat_civil", "proffession", "residence_quarter", "residence_zone", "CNI", "payment_method", "payment_serial")
        fields = ("zone", "residence_quarter","child_name","child_birth",
            "child_mother","first_witness","second_witness")

    # def clean_zone(self, *arg,**kwargs):
    #     try:
    #         name = self.cleaned_data.get("zone")
    #         zone = Zone.objects.get(name=name)
    #         return zone
    #     except:
    #         raise forms.ValidationError("this zone is unknown")

    # def clean_residence_quarter(self, *arg,**kwargs):
    #     try:
    #         name = self.cleaned_data.get("residence_quarter").split()[0]
    #         zone = self.cleaned_data.get("residence_quarter").split()[-1]
    #         quarter = Quarter.objects.get(name=name, zone__name=zone)
    #         return quarter
    #     except Exception as e:
    #         raise forms.ValidationError("this quarter is unknown")

    # def clean_child_mother(self, *arg, **kwargs):
    #     try:
    #         first_name = self.cleaned_data.get("clean_mother").split()[0]
    #         last_name = self.cleaned_data.get("clean_mother").split()[-1]
    #         profile = Profile.objects.get(user__first_name=first_name, user__last_name=last_name)
    #         return profile
    #     except Exception as e:
    #         raise forms.ValidationError("unknown user")

    # def clean_first_witness(self, *arg, **kwargs):
    #     try:
    #         first_name = self.cleaned_data.get("first_witness").split()[0]
    #         last_name = self.cleaned_data.get("first_witness").split()[-1]
    #         profile = Profile.objects.get(user__first_name=first_name, user__last_name=last_name)
    #         return profile
    #     except Exception as e:
    #         raise forms.ValidationError("unknown user")

    # def clean_second_witness(self, *arg, **kwargs):
    #     try:
    #         first_name = self.cleaned_data.get("second_witness").split()[0]
    #         last_name = self.cleaned_data.get("second_witness").split()[-1]
    #         profile = Profile.objects.get(user__first_name=first_name, user__last_name=last_name)
    #         return profile
    #     except Exception as e:
    #         raise forms.ValidationError("unknown user")




