from django import forms
from .models import *
from apps.base.models import *
from datetime import date

class DocumentForm(forms.ModelForm):
    zone = forms.ModelChoiceField(
        widget = forms.Select(
            attrs = {'placeholder': 'Zone', 'class': 'form-control', 'id':'zones'}),
        label = 'Zone',
        queryset = Zone.objects.all())
    
    date = forms.DateField(
        widget=forms.SelectDateWidget(
            years=range(2020, date.today().year),
            attrs={'placeholder':'yyyy-mm-dd ', 'class':'form-control',
                'style':'width: auto;display: inline-block;'}),
        label='date')

    comparant_1 = forms.CharField(
        widget = forms.TextInput(
            attrs = {'placeholder': 'CNI premier du comparant', 
                    'class': 'form-control check_cni'}),
        label = 'CNI du premier comparant') 
        
    comparant_2 = forms.CharField(
        widget = forms.TextInput(
            attrs = {'placeholder': 'CNI second du comparant', 
                    'class': 'form-control check_cni'}),
        label = 'CNI du second comparant',
        required=False) 
        
    comparant_3 = forms.CharField(
        widget = forms.TextInput(
            attrs = {'placeholder': 'CNI troisième du comparant', 
                    'class': 'form-control check_cni'}),
        label = 'CNI du troisième comparant',
        required=False) 

    class Meta:
        model = Document
        fields = ("zone", "date", "comparant_1", "comparant_2","comparant_3")

    def clean_comparant_1(self, *arg,**kwargs):
        try:
            CNI = self.cleaned_data.get("comparant_1")
            eval(CNI)
            comparant = Profile.objects.get(CNI=CNI)
            return comparant
        except:
            raise forms.ValidationError("Ce comparant n'est pas abonné")

    def clean_comparant_2(self, *arg,**kwargs):
        CNI1 = self.cleaned_data.get("comparant_1")
        CNI = self.cleaned_data.get("comparant_2")
        try:
            eval(CNI)
        except Exception as e:
            raise forms.ValidationError("CNI invalide")

        if CNI.strip() == CNI1.CNI:
            raise forms.ValidationError("Duplication de comparant")
        try:
            comparant = Profile.objects.get(CNI=CNI)
            return comparant
        except:
            raise forms.ValidationError("Ce comparant n'est pas abonné")

    def clean_comparant_3(self, *arg,**kwargs):
        CNI1 = self.cleaned_data.get("comparant_1")
        CNI2 = self.cleaned_data.get("comparant_2")
        CNI = self.cleaned_data.get("comparant_3")
        if not CNI.strip() or CNI in (CNI2, CNI1):
            return None
        try:
            comparant = Profile.objects.get(CNI=CNI)
            return comparant
        except:
            raise forms.ValidationError("Ce comparant n'est pas abonné")

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