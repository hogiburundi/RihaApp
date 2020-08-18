from django import forms
from .models import *
from apps.base.models import *
from datetime import date

class DocumentForm(forms.ModelForm):
        
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
        
    day_month_year = forms.DateField(
        widget=forms.SelectDateWidget(
            years=range(1950, date.today().year+1),
            attrs={'placeholder':'yyyy-mm-dd ', 'class':'form-control',
                'style':'width: 50%;'}),
        label='Date of Day')

    child_date = forms.DateField(
        widget=forms.SelectDateWidget(
            years=range(1950, date.today().year+1),
            attrs={'placeholder':'yyyy-mm-dd ', 'class':'form-control',
                'style':'width: 50%;display:'}),
        label='Child Day')

    search_place = forms.ModelChoiceField(
        widget = forms.Select(
            attrs = {'placeholder': 'Place to look for the document.', 
                    'class': 'form-control',
                    'id':'search_place'}),
        label = 'Place to look for the document.',
        queryset = Quarter.objects.all())

    witness1 = forms.CharField(
        widget = forms.TextInput(
            attrs = {'placeholder': 'First Witness CNI',
                    'class': 'form-control'}),
        label = 'First Witness CNI')  
              
    witness2 = forms.CharField(
        widget = forms.TextInput(
            attrs = {'placeholder': 'Second Witness CNI',
                    'class': 'form-control'}),
        label = 'Second Witness CNI')
        
    child = forms.CharField( 
        widget = forms.TextInput(
            attrs = {'placeholder': 'Child CNI',
                    'class': 'form-control'}),
        label = 'Child CNI')

    wife = forms.CharField(
        widget = forms.TextInput(
            attrs = {'placeholder': 'Wife CNI',
                    'class': 'form-control'}),
        label = 'Wife CNI')


    class Meta:
        model = Document
        fields = ("search_place", "volume", "acte", "day_month_year", "child_date","witness1","witness2","child","wife")

    def clean_witness1(self, *arg,**kwargs):
        try:
            CNI = self.cleaned_data.get("witness1")
            comparant = Profile.objects.get(CNI=CNI)
            return comparant
        except:
            raise forms.ValidationError("CNI does not exist")

    def clean_witness2(self, *arg,**kwargs):
        try:
            CNI = self.cleaned_data.get("witness2")
            comparant = Profile.objects.get(CNI=CNI)
            return comparant
        except:
            raise forms.ValidationError("CNI does not exist")

    def clean_child(self, *arg,**kwargs):
        try:
            CNI = self.cleaned_data.get("child")
            comparant = Profile.objects.get(CNI=CNI)
            return comparant
        except:
            raise forms.ValidationError("CNI does not exist")

    def clean_wife(self, *arg,**kwargs):
        try:
            CNI = self.cleaned_data.get("wife")
            comparant = Profile.objects.get(CNI=CNI)
            return comparant
        except:
            raise forms.ValidationError("CNI does not exist")


class ValidationForm(forms.Form):
    cni_recto = forms.BooleanField(widget=forms.CheckboxInput(),
        label='CNI recto', required=False)
    cni_verso = forms.BooleanField(widget=forms.CheckboxInput(),
        label='CNI verso', required=False)
    cni_recto_1 = forms.BooleanField(widget=forms.CheckboxInput(),
        label='CNI recto comparant 1', required=False)
    cni_verso_1 = forms.BooleanField(widget=forms.CheckboxInput(),
        label='CNI verso comparant 1', required=False)
    cni_recto_2 = forms.BooleanField(widget=forms.CheckboxInput(),
        label='CNI recto comparant 2', required=False)
    cni_verso_2 = forms.BooleanField(widget=forms.CheckboxInput(),
        label='CNI verso comparant 2', required=False)
    payment = forms.BooleanField(
        widget=forms.CheckboxInput(attrs={'placeholder':'le code de paiement '}),
        label='le code de paiement', required=False)
    cni = forms.BooleanField(
        widget=forms.CheckboxInput(attrs={'placeholder':'numero CNI '}),
        label='numero CNI', required=False)