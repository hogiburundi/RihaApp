from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

class Profile(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE)
	avatar = models.ImageField(upload_to='avatars/', null=True, blank=True)
	nationnalite = models.CharField(max_length=64)
	quarter = models.ForeignKey('Quarter', null=True, blank=True, on_delete=models.SET_NULL)
	address = models.CharField(max_length=64)
	CNI = models.CharField(max_length=64, null=True, blank=True)
	# father = models.ForeignKey(User, related_name='father', null=True, blank=True, on_delete=models.SET_NULL)
	# mother = models.ForeignKey(User, related_name='mother', null=True, blank=True, on_delete=models.SET_NULL)
	father = models.CharField(max_length=64, null=True, blank=True)
	mother = models.CharField(max_length=64, null=True, blank=True)
	birthdate = models.DateField()
	is_married = models.BooleanField()
	cni_recto = models.ImageField(upload_to='cnis/', null=True, blank=True)
	cni_verso = models.ImageField(upload_to='cnis/', null=True, blank=True)
	job = models.CharField(max_length=64)

	def __str__(self):
		return f"{self.user.last_name} {self.user.first_name}"

class Zone(models.Model):
	name = models.CharField(max_length=64)
	commune = models.ForeignKey('Commune', on_delete=models.CASCADE)
	leader = models.ForeignKey(User, verbose_name="zone leader", null=True, blank=True, on_delete=models.SET_NULL)
	ecocash = models.CharField(max_length=64)
	lumicash = models.CharField(max_length=64)
	bcb = models.CharField(max_length=64)

	def __str__(self):
		return f"{self.name} - {self.commune.province}"

class Province(models.Model):
	name = models.CharField(max_length=64)
	leader = models.ForeignKey(User, verbose_name="province leader", null=True, blank=True, on_delete=models.SET_NULL)
	ecocash = models.CharField(max_length=64)
	lumicash = models.CharField(max_length=64)
	bcb = models.CharField(max_length=64)

	def __str__(self):
		return f"{self.name}"
	
class Commune(models.Model):
	name = models.CharField(max_length=64)
	province = models.ForeignKey('Province', on_delete=models.CASCADE)
	leader = models.ForeignKey(User, verbose_name="commune leader", null=True, blank=True, on_delete=models.SET_NULL)
	ecocash = models.CharField(max_length=64)
	lumicash = models.CharField(max_length=64)
	bcb = models.CharField(max_length=64)

	def __str__(self):
		return f"{self.name} - {self.province}"

class Quarter(models.Model):
	name = models.CharField(max_length=64)
	zone = models.ForeignKey('Zone', on_delete=models.CASCADE)
	leader = models.ForeignKey(User, verbose_name="quarter leader", null=True, blank=True, on_delete=models.SET_NULL)
	ecocash = models.CharField(max_length=64)
	lumicash = models.CharField(max_length=64)
	bcb = models.CharField(max_length=64)

	def __str__(self):
		return f"{self.name} - {self.zone.name}"

PAYMENTS = ( 
    ("ecocash", "Ecocash"), 
    ("lumicash", "Lumicash"), 
    ("bcb", "BCB"), 
) 

class ModelPayement(models.Model):
	type_payement = models.CharField(choices=PAYMENTS)
	id_transaction = models.CharField(max_length=64)
	bordereau = models.ImageField(upload_to='bordereaux/', null=True, blank=True)
	date = models.DateTimeField(default=timezone.now)
	
	class Meta:
		abstract = True

class PayementQuarter(ModelPayement):
	quarter = models.ForeignKey('Quarter', on_delete=models.CASCADE)

	def __str__():
		return f"{self.quarter} - {self.date} : {self.id_transaction}"

class PayementCommune(ModelPayement):
	commune = models.ForeignKey('Commune', on_delete=models.CASCADE)
	
	def __str__():
		return f"{self.commune} - {self.date} : {self.id_transaction}"

class PayementProvince(ModelPayement):
	province = models.ForeignKey('Province', on_delete=models.CASCADE)
	
	def __str__():
		return f"{self.province} - {self.date} : {self.id_transaction}"

class PayementZone(ModelPayement):
	zone = models.ForeignKey('Zone', on_delete=models.CASCADE)
	
	def __str__():
		return f"{self.zone} - {self.date} : {self.id_transaction}"