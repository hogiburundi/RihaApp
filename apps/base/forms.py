from .models import *
from django import forms
from datetime import date

class ConnexionForm(forms.Form):
	username = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Username ','class':'form-control'}))
	password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder':'Password ', 'type':'password','class':'form-control'}))

class PasswordForm(forms.Form):
	password = forms.CharField( widget=forms.PasswordInput(attrs={'placeholder':'Password ','class':'form-control'}), label='Password')
	password2 = forms.CharField( widget=forms.PasswordInput(attrs={'placeholder':'Confirm password ','class':'form-control'}), label='Confirm password')

class Register2Form(forms.Form):
	cni_recto = forms.ImageField( widget=forms.FileInput(attrs={'placeholder':'CNI Picture 1','class':'form-control'}), label='CNI Picture 1')
	cni_verso = forms.ImageField( widget=forms.FileInput(attrs={'placeholder':'CNI Picture 2','class':'form-control'}), label='CNI Picture 2')

class ProfileForm(forms.ModelForm):
	gender = forms.ChoiceField(
		widget=forms.Select(
			attrs={'placeholder':'Gender ','class':'form-control'}),
		label='Gender',
		choices=GENDERS)
	nationnalite = forms.CharField( widget=forms.TextInput(attrs={'placeholder':'Nationnalite ','class':'form-control'}), label='Nationnalite')
	quarter = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Quarter ','class':'form-control', 'list':'quarters'}), label='Quarter')
	address = forms.CharField( widget=forms.TextInput(attrs={'placeholder':'Address ','class':'form-control'}), label='Address')
	CNI = forms.CharField( widget=forms.TextInput(attrs={'placeholder':'CNI ','class':'form-control'}), label='CNI')
	date_delivrated = forms.DateField( widget=forms.TextInput(attrs={'placeholder':'date delivrated ','class':'form-control'}), label='Date ')
	father = forms.CharField( widget=forms.TextInput(attrs={'placeholder':'Father ','class':'form-control'}), label='Father')
	mother = forms.CharField( widget=forms.TextInput(attrs={'placeholder':'Mother ','class':'form-control'}), label='Mother')
	birthdate = forms.DateField(
		widget=forms.SelectDateWidget(
			years=range(1960, date.today().year),
			attrs={'placeholder':'yyyy-mm-dd ',
				'class':'form-control',
				'style':'width: auto;display: inline-block;'}),
		label='Birthdate')
	colline_natal  = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'colline natale'}), label="colline natale")
	commune_natal  = forms.CharField( widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'commune natale'}), label="commune natale")
	province_natal = forms.CharField( widget=forms.TextInput(attrs={'placeholder':'Province natale ','class':'form-control'}), label='Province natale')

	is_married = forms.BooleanField(
		widget=forms.CheckboxInput(
			attrs={'placeholder':'Married '}),
		label='Married',
		required=False)
	job = forms.CharField(
		widget=forms.TextInput(
			attrs={'placeholder':'Job ','class':'form-control'}),
		label='Job', required=False)
	prefix = forms.CharField(
		widget=forms.TextInput(
			attrs={'placeholder':'Example : Hon. Dr. Ir. ','class':'form-control'}),
		label='Prefix', required=False)
	
	def clean_quarter(self, *arg,**kwargs):
		try:
			name = self.cleaned_data.get("quarter").split()[0]
			zone = self.cleaned_data.get("quarter").split()[-1]
			quarter = Quarter.objects.get(name=name, zone__name=zone)
			return quarter
		except Exception as e:
			raise forms.ValidationError("this quarter is unknown")	

	class Meta:
		model = Profile
		fields = ("gender", "nationnalite", "quarter", "address", "father", "mother", "birthdate", "is_married", "job", "CNI", 'date_delivrated','colline_natal', 'commune_natal', 'province_natal')

class RegisterForm(forms.Form):
	telephone = forms.CharField( widget=forms.TextInput(attrs={'placeholder':'your phone number','class':'form-control'}), label='Phone number')
	firstname = forms.CharField( widget=forms.TextInput(attrs={'placeholder':'Firstname ','class':'form-control'}), label='Firstname')
	lastname = forms.CharField( widget=forms.TextInput(attrs={'placeholder':'Lastname ','class':'form-control'}), label='Lastname')
	password = forms.CharField( widget=forms.PasswordInput(attrs={'placeholder':'Password ','class':'form-control'}), label='Password')
	password2 = forms.CharField( widget=forms.PasswordInput(attrs={'placeholder':'Confirm password ','class':'form-control'}), label='Confirm password')

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

class ModelPayementFormMixin(forms.Form):
	type_payement = forms.ChoiceField(
		widget=forms.Select(
			attrs={'placeholder':'payment method','class':'form-control'}
		),
		label='Payment method',
		choices=PAYMENTS
	)
	id_transaction = forms.CharField(
		widget=forms.TextInput(
			attrs={'placeholder':'Transaction ID','class':'form-control'}
		),
		label='Transaction ID'
	)
	bordereau = forms.ImageField(
		widget=forms.FileInput(
			attrs={'placeholder':'bordereau','class':'form-control'}
		),
		label='bordereau',
		required=False
	)

	def clean_id_transaction(self, *arg,**kwargs):
		id_transaction = self.cleaned_data.get("id_transaction")
		if UsedSN.objects.filter(id_transaction = id_transaction):
			raise forms.ValidationError("this serial is already used")
		return id_transaction


class PaymentQuarterForm(forms.ModelForm, ModelPayementFormMixin):
	quarter = forms.CharField(
		widget = forms.TextInput(
			attrs = {'placeholder': 'Quarter', 
				'class': 'form-control',
				'list':'quarters'}),
		label = 'Quarter')

	def __init__(self, *args, **kwargs):
		super(PaymentQuarterForm, self).__init__(*args, **kwargs)

	class Meta:
		model = PaymentQuarter
		fields = ( "type_payement", "id_transaction", "bordereau", "date", "quarter")

class PaymentCommuneForm(forms.ModelForm, ModelPayementFormMixin):
	commune = forms.CharField(
		widget = forms.TextInput(
			attrs = {'placeholder': 'Commune', 
				'class': 'form-control', 
				'list':'communes'}),
		label = 'Commune')

	def __init__(self, *args, **kwargs):
		super(PaymentCommuneForm, self).__init__(*args, **kwargs)

	class Meta:
		model = PaymentCommune
		fields = ( "type_payement", "id_transaction", "bordereau", "date", "commune")

class PaymentProvinceForm(forms.ModelForm, ModelPayementFormMixin):
	province = forms.CharField(
		widget = forms.TextInput(
			attrs = {'placeholder': 'Province', 
				'class': 'form-control', 
				'list':'provinces'}),
		label = 'Province')

	def __init__(self, *args, **kwargs):
		super(PaymentProvinceForm, self).__init__(*args, **kwargs)

	class Meta:
		model = PaymentProvince
		fields = ( "type_payement", "id_transaction", "bordereau", "date", "province")

class PaymentZoneForm(ModelPayementFormMixin, forms.ModelForm):
	# zone = forms.CharField(
	# 	widget = forms.TextInput(
	# 		attrs = {'placeholder': 'Zone', 
	# 			'class': 'form-control', 
	# 			'list':'zones'}),
	# 	label = 'Zone')

	def __init__(self, *args, **kwargs):
		super(PaymentZoneForm, self).__init__(*args, **kwargs)

	class Meta:
		model = PaymentZone
		fields = ( "type_payement","id_transaction", "bordereau")