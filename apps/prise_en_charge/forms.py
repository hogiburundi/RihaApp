from django import forms
from .models import *
from apps.base.models import *

class DocumentForm(forms.ModelForm):
        
    mrs = forms.CharField(
        widget = forms.TextInput(
            attrs = {'placeholder': 'Wife of taker in charge(Mrs.)', 
                    'class': 'form-control'}),
        label = 'Wife of taker in charge (Mrs.)')

    search_place = forms.ModelChoiceField(
        widget = forms.Select(
            attrs = {'placeholder': 'Place to look for the document.', 
                    'class': 'form-control',
                    'id':'search_place'}),
        label = 'Place to look for the document.',
        queryset = Quarter.objects.all())


    class Meta:
        model = Document
        fields = ("search_place","mrs")

    def clean_mrs(self, *arg,**kwargs):
        try:
            CNI = self.cleaned_data.get("mrs")
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
        label='CNI recto femme', required=False)
    cni_verso_1 = forms.BooleanField(widget=forms.CheckboxInput(),
        label='CNI verso ffemme', required=False)
    payment = forms.BooleanField(
        widget=forms.CheckboxInput(attrs={'placeholder':'le code de paiement '}),
        label='Le code de paiement', required=False)
    cni = forms.BooleanField(
        widget=forms.CheckboxInput(attrs={'placeholder':'numero CNI femme '}),
        label='Numéro CNI femme', required=False)
        