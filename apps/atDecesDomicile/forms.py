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

    dead_man =  forms.CharField(
        widget = forms.TextInput(
            attrs = {'placeholder': "Nom Défunt", 
                    'class': 'form-control',
                    'list':'profiles'}),
        label = "Nom complet du Défunt")

    residence_quarter_DM = forms.CharField(
        widget = forms.TextInput(
            attrs = {'placeholder': 'Residence Quarter', 
                    'class': 'form-control',
                    'list':'quarters'}),
        label = 'Quartier de residence actuelle')

    DM_date = forms.DateField(
        widget=forms.SelectDateWidget(
            years=range(1960, date.today().year),
            attrs={'placeholder':'yyyy-mm-dd ',
                'class':'form-control',
                'style':'width: auto;display: inline-block;'}),
        label='Date de décès')


    first_witness = forms.CharField(
        widget = forms.TextInput(
            attrs = {'placeholder': 'Temoin', 
                    'class': 'form-control', 
                    'list':'profiles'}),
        label = "1er Témoin")

    second_witness = forms.CharField(
        widget = forms.TextInput(
            attrs = {'placeholder': 'Temoin', 
                    'class': 'form-control', 
                    'list':'profiles'}),
        label = "2ème Témoin")

    quarter_leader = forms.CharField(
        widget = forms.TextInput(
            attrs = {'placeholder': 'Quartier', 
                    'class': 'form-control', 
                    'list':'profiles'}),
        label = "Chef de quartier")

    class Meta:
        model = Document
        # fields = ("zone_leader", "zone", "beneficiary", "father", "mother", "birth_quarter", "birth_year", "birth_commune", "birth_province", "nationality", "etat_civil", "proffession", "residence_quarter", "residence_zone", "CNI", "payment_method", "payment_serial")
        fields = ("zone", "dead_man","residence_quarter_DM","DM_date",
            "first_witness","second_witness","quarter_leader")

    def clean_zone(self, *arg,**kwargs):
        try:
            name = self.cleaned_data.get("zone")
            zone = Zone.objects.get(name=name)
            return zone
        except:
            raise forms.ValidationError("this zone is unknown")

    def clean_dead_man(self, *arg, **kwargs):
        try:
            first_name = self.cleaned_data.get("dead_man").split()[0]
            last_name = self.cleaned_data.get("dead_man").split()[-1]
            profile = Profile.objects.get(user__first_name=first_name, user__last_name=last_name)
            return profile
        except Exception as e:
            raise forms.ValidationError("unknown user")

    def clean_residence_quarter_DM(self, *arg,**kwargs):
        try:
            name = self.cleaned_data.get("residence_quarter_DM").split()[0]
            zone = self.cleaned_data.get("residence_quarter_DM").split()[-1]
            quarter = Quarter.objects.get(name=name, zone__name=zone)
            return quarter
        except Exception as e:
            raise forms.ValidationError("this quarter is unknown")

    def clean_first_witness(self, *arg, **kwargs):
        try:
            first_name = self.cleaned_data.get("first_witness").split()[0]
            last_name = self.cleaned_data.get("first_witness").split()[-1]
            profile = Profile.objects.get(user__first_name=first_name, user__last_name=last_name)
            return profile
        except Exception as e:
            raise forms.ValidationError("unknown user")

    def clean_second_witness(self, *arg, **kwargs):
        try:
            first_name = self.cleaned_data.get("second_witness").split()[0]
            last_name = self.cleaned_data.get("second_witness").split()[-1]
            profile = Profile.objects.get(user__first_name=first_name, user__last_name=last_name)
            return profile
        except Exception as e:
            raise forms.ValidationError("unknown user")

    def clean_quarter_leader(self, *arg, **kwargs):
        try:
            first_name = self.cleaned_data.get("quarter_leader").split()[0]
            last_name = self.cleaned_data.get("quarter_leader").split()[-1]
            profile = Profile.objects.get(user__first_name=first_name, user__last_name=last_name)
            return profile
        except Exception as e:
            raise forms.ValidationError("unknown user")




