from .models import *
from django import forms
from datetime import date

class ConnexionForm(forms.Form):
	username = forms.CharField(widget=forms.TextInput(
		attrs={'placeholder':'Username ','class':'form-control round'}))
	password = forms.CharField(widget=forms.PasswordInput(
		attrs={'placeholder':'Password ', 'type':'password','class':'form-control round'}))
	
	def clean_username(self, *arg,**kwargs):
		username = self.cleaned_data.get("username")
		if(username.isdigit() and len(username)==8):
			return username
		else :
			raise forms.ValidationError("must be a valid burudian phone number")

class PasswordForm(forms.Form):
	password = forms.CharField( widget=forms.PasswordInput(attrs={'placeholder':'Password ','class':'form-control'}), label='Password')
	password2 = forms.CharField( widget=forms.PasswordInput(attrs={'placeholder':'Confirm password ','class':'form-control'}), label='Confirm password')

class Register2Form(forms.ModelForm):
	CNI = forms.CharField(widget=forms.TextInput(
			attrs={'placeholder':'CNI ','class':'form-control'}),
		label='Carte nationnal d\'identité', required=False)
	#zone_delivery_CNI = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Zone ','class':'form-control', 'list':'zones'}), label='Zone de délivraison')
	date_delivrated = forms.DateField(widget=forms.TextInput(
			attrs={'placeholder':'date delivrated ', 'type':'date',
				'class':'form-control',}),
		label='Délivrée le', required=False,initial=date.today())

	place_delivrated = forms.CharField(
		widget=forms.TextInput(
			attrs={'placeholder':'province de livraison','class':'form-control'}),
		label='Délivrée à', required=False)
	cni_recto = forms.ImageField( widget=forms.FileInput(
			attrs={'placeholder':'CNI Picture 1','class':'form-control'}),
		label='CNI Picture 1', required=False)
	cni_verso = forms.ImageField( widget=forms.FileInput(
			attrs={'placeholder':'CNI Picture 2','class':'form-control'}),
		label='CNI Picture 2', required=False)
	
	class Meta:
		model = Profile
		fields = ("CNI", 'date_delivrated', 'place_delivrated', 'cni_recto', 'cni_verso')


	def clean_CNI(self, *arg,**kwargs):
		try:
			CNI = self.cleaned_data.get("CNI")
			eval(CNI)
			return CNI
		except:
			raise forms.ValidationError("Ce CNI est invalide")

class ProfileForm(forms.ModelForm):
	gender = forms.ChoiceField(
		widget=forms.Select(
			attrs={'placeholder':'Gender ','class':'form-control'}),
		label='Gender',
		choices=GENDERS)

	nationnalite = forms.CharField( widget=forms.TextInput(attrs={'placeholder':'Nationnalite ','class':'form-control'}), label='Nationnalite')
	quarter = forms.ModelChoiceField(widget = forms.Select(
			attrs = {'placeholder': 'Quarter', 'class': 'form-control','id':'quarters'}),
		label = 'Quartier/Colline de naissance',
		queryset = Quarter.objects.all())
	residence = forms.ModelChoiceField( widget = forms.Select(
			attrs = {'placeholder': 'Residence Quarter', 'class': 'form-control','id':'residences'}),
		label = 'Residence Quarter',
		queryset = Quarter.objects.all())
	address = forms.CharField( widget=forms.TextInput(attrs={'placeholder':'Address ','class':'form-control'}), label='Address')

	father = forms.CharField( widget=forms.TextInput(attrs={'placeholder':'Father ','class':'form-control'}), label='Father')
	mother = forms.CharField( widget=forms.TextInput(attrs={'placeholder':'Mother ','class':'form-control'}), label='Mother')
	birthdate = forms.DateField(
		widget=forms.TextInput(
			attrs={'placeholder':'yyyy-mm-dd ', 'type':'date', 'class':'form-control'}),
		label='Birthdate')
	job = forms.CharField(
		widget=forms.TextInput(
			attrs={'placeholder':'Job ','class':'form-control'}),
		label='Job', required=False)
	prefix = forms.CharField(
		widget=forms.TextInput(
			attrs={'placeholder':'Example : Hon. Dr. Ir. ','class':'form-control'}),
		label='Prefix', required=False)
		
	is_married = forms.BooleanField(
		widget=forms.CheckboxInput( attrs={'placeholder':'Married '}),
		label='Married', required=False)

	class Meta:
		model = Profile
		fields = ("gender", "nationnalite", "quarter", "address", "father", "mother", "birthdate", "job", "is_married", "residence")

class RegisterForm(forms.Form):
	telephone = forms.CharField( widget=forms.NumberInput(
			attrs={'placeholder':'your phone number','class':'form-control col-md-12'}),
		label='Phone number')
	firstname = forms.CharField( widget=forms.TextInput(
			attrs={'placeholder':'Firstname ','class':'form-control'}),
		label='Firstname')
	lastname = forms.CharField( widget=forms.TextInput(
			attrs={'placeholder':'Lastname ','class':'form-control'}),
		label='Lastname')
	password = forms.CharField( widget=forms.PasswordInput(
			attrs={'placeholder':'Password ','class':'form-control'}),
		label='Password')
	password2 = forms.CharField( widget=forms.PasswordInput(
			attrs={'placeholder':'Confirm password ','class':'form-control'}),
		label='Confirm password')

	def clean_password2(self, *arg,**kwargs):
		try:
			password = self.cleaned_data.get("password")
			password2 = self.cleaned_data.get("password2")
			if(password == password2):
				return password
			else :
				raise forms.ValidationError("confirmation password must same as password")
		except Exception as e:
			raise forms.ValidationError("confirmation password must same as password")
	
	def clean_telephone(self, *arg,**kwargs):
		telephone = self.cleaned_data.get("telephone")
		try:
			user = User.objects.get(username=telephone)
		except Exception as e:
			return telephone
		raise forms.ValidationError("user already exists")
			

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