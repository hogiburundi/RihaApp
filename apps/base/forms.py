from .models import *
from django import forms
from datetime import date

class ConnexionForm(forms.Form):
	username = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Username ','class':'form-control'}))
	password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder':'Password ', 'type':'password','class':'form-control'}))

class PasswordForm(forms.Form):
	password = forms.CharField( widget=forms.PasswordInput(attrs={'placeholder':'Password ','class':'form-control'}), label='Password')
	password2 = forms.CharField( widget=forms.PasswordInput(attrs={'placeholder':'Confirm password ','class':'form-control'}), label='Confirm password')

class RegisterForm(forms.Form):
	username = forms.CharField( widget=forms.TextInput(attrs={'placeholder':'Username ','class':'form-control'}), label='Username')
	firstname = forms.CharField( widget=forms.TextInput(attrs={'placeholder':'Firstname ','class':'form-control'}), label='Firstname')
	lastname = forms.CharField( widget=forms.TextInput(attrs={'placeholder':'Lastname ','class':'form-control'}), label='Lastname')
	password = forms.CharField( widget=forms.PasswordInput(attrs={'placeholder':'Password ','class':'form-control'}), label='Password')
	password2 = forms.CharField( widget=forms.PasswordInput(attrs={'placeholder':'Confirm password ','class':'form-control'}), label='Confirm password')
	
	avatar = forms.ImageField( widget=forms.FileInput(attrs={'placeholder':'Avatar ','class':'form-control'}), label='Avatar')
	nationnalite = forms.CharField( widget=forms.TextInput(attrs={'placeholder':'Nationnalite ','class':'form-control'}), label='Nationnalite')
	quarter = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Quarter ','class':'form-control', 'list':'quarters'}), label='Quarter')
	address = forms.CharField( widget=forms.TextInput(attrs={'placeholder':'Address ','class':'form-control'}), label='Address')
	CNI = forms.CharField( widget=forms.TextInput(attrs={'placeholder':'CNI ','class':'form-control'}), label='CNI')
	father = forms.CharField( widget=forms.TextInput(attrs={'placeholder':'Father ','class':'form-control'}), label='Father')
	mother = forms.CharField( widget=forms.TextInput(attrs={'placeholder':'Mother ','class':'form-control'}), label='Mother')
	birthdate = forms.DateField( widget=forms.SelectDateWidget(years=range(1960, date.today().year), attrs={'placeholder':'yyyy-mm-dd ','class':'form-control inline-form-control'}), label='Birthdate')
	is_married = forms.BooleanField( widget=forms.CheckboxInput(attrs={'placeholder':'Married '}), label='Married')
	job = forms.CharField( widget=forms.TextInput(attrs={'placeholder':'Job ','class':'form-control'}), label='Job')
	
	def clean_quarter(self, *arg,**kwargs):
		try:
			name = self.cleaned_data.get("quarter").split()[0]
			zone = self.cleaned_data.get("quarter").split()[-1]
			quarter = Quarter.objects.get(name=name, zone__name=zone)
			return quarter
		except Exception as e:
			raise forms.ValidationError("this quarter is unknown")	

	def clean_password2(self, *arg,**kwargs):
		try:
			password = self.cleaned_data.get("password")
			password2 = self.cleaned_data.get("password2")
			print(password, password2)
			if(password == password2):
				return password
			else :
				raise forms.ValidationError("confirmation password must same as password")
		except Exception as e:
			raise forms.ValidationError("confirmation password must same as password")