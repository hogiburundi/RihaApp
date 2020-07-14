from django import forms
from .models import *
from apps.base.models import *
from datetime import date

class DocumentForm(forms.ModelForm):

    zone = forms.CharField(
        widget = forms.TextInput(
            attrs = {'placeholder': 'Zone', 
                    'class': 'form-control', 
                    'list':'zones'}),
        label = 'Zone de residence actuelle')

    residence_quarter = forms.CharField(
        widget = forms.TextInput(
            attrs = {'placeholder': 'Residence Quarter', 
                    'class': 'form-control',
                    'list':'quarters'}),
        label = 'Quartier de residence actuelle')

    child_name =  forms.CharField(
        widget = forms.TextInput(
            attrs = {'placeholder': "Nom Enfant", 
                    'class': 'form-control',}),
        label = "Nom complet de l'enfant")

    child_birth = forms.DateField(
        widget=forms.SelectDateWidget(
            years=range(1960, date.today().year
                ), attrs={'placeholder':'yyyy-mm-dd ',
            'class':'form-control inline-form-control'}),
             label="Année de naissance de l'enfant")

    child_birth_quarter = forms.CharField(
        widget = forms.TextInput(
            attrs = {'placeholder': 'Quartier naissance', 
                    'class': 'form-control', 
                    'list':'quarters'}),
        label = "Quartier de naissance de l'enfant")

    child_mother = forms.CharField(
        widget = forms.TextInput(
            attrs = {'placeholder': 'Mère', 
                    'class': 'form-control', 
                    'list':'profiles'}),
        label = "Mère de l'enafant")

    first_witness = forms.CharField(
        widget = forms.TextInput(
            attrs = {'placeholder': 'Mère', 
                    'class': 'form-control', 
                    'list':'profiles'}),
        label = "Mère de l'enafant")

    second_witness = forms.CharField(
        widget = forms.TextInput(
            attrs = {'placeholder': 'Mère', 
                    'class': 'form-control', 
                    'list':'profiles'}),
        label = "Mère de l'enafant")

    supervisor = forms.CharField(
        widget = forms.TextInput(
            attrs = {'placeholder': 'Mère', 
                    'class': 'form-control', 
                    'list':'profiles'}),
        label = "Mère de l'enafant")

    class Meta:
        model = Document
        # fields = ("zone_leader", "zone", "beneficiary", "father", "mother", "birth_quarter", "birth_year", "birth_commune", "birth_province", "nationality", "etat_civil", "proffession", "residence_quarter", "residence_zone", "CNI", "payment_method", "payment_serial")
        fields = ("zone", "residence_quarter","child_name","child_birth",
            "child_mother","first_witness","second_witness","supervisor")

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

    def clean_mother(self, *arg, **kwargs):
        try:
            first_name = self.cleaned_data.get("clean_mother").split()[0]
            last_name = self.cleaned_data.get("clean_mother").split()[-1]
            profile = Profile.objects.get(user__first_name=first_name, user__last_name=last_name)
            return profile
        except Exception as e:
            raise forms.ValidationError("unknown user")

    def first_witness(self, *arg, **kwargs):
        try:
            first_name = self.cleaned_data.get("first_witness").split()[0]
            last_name = self.cleaned_data.get("first_witness").split()[-1]
            profile = Profile.objects.get(user__first_name=first_name, user__last_name=last_name)
            return profile
        except Exception as e:
            raise forms.ValidationError("unknown user")

    def second_witness(self, *arg, **kwargs):
        try:
            first_name = self.cleaned_data.get("second_witness").split()[0]
            last_name = self.cleaned_data.get("second_witness").split()[-1]
            profile = Profile.objects.get(user__first_name=first_name, user__last_name=last_name)
            return profile
        except Exception as e:
            raise forms.ValidationError("unknown user")

    def supervisor(self, *arg, **kwargs):
        try:
            first_name = self.cleaned_data.get("supervisor").split()[0]
            last_name = self.cleaned_data.get("supervisor").split()[-1]
            profile = Profile.objects.get(user__first_name=first_name, user__last_name=last_name)
            return profile
        except Exception as e:
            raise forms.ValidationError("unknown user")




