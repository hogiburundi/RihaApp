from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from apps.base.models import *

class Document(models.Model):
	user = models.ForeignKey(User, related_name="banmariage_groom", null=True, on_delete=models.SET_NULL)
	bride = models.ForeignKey(Profile, related_name="banmariage_bride", null=True, on_delete=models.SET_NULL)
	zone = models.ForeignKey(Zone, related_name="banmariage_zone", max_length=64, null=True, on_delete=models.SET_NULL)
	residence_quarter = models.ForeignKey(Quarter, related_name="banmariage_residence", max_length=64, null=True, on_delete=models.SET_NULL)
	date = models.DateField(default=timezone.now)
	rejection_msg = models.TextField(null=True, blank=True)
	secretary_validated = models.BooleanField(null=True)
	ready = models.BooleanField(default=False)
	zone_payment = models.ForeignKey(PaymentZone, related_name="banmariage_province_payment", blank=True, null=True, on_delete=models.SET_NULL)



	def requirements():
		return ["copie de contrat d'execution d'un travail quelconque", ]

	def price(self):
		try:
			return PriceHistory.objects.filter(zone=self.zone).last().total()
		except:
			return 0

class PriceHistory(models.Model):
	date = models.DateField()
	zone = models.ForeignKey(Zone, related_name="banmariage_price_province", on_delete=models.CASCADE)
	zone_price = models.IntegerField(default=0)
	
	def total(self):
		return self.zone_price



class Incognito(models.Model):
	
	incognito_gender= models.CharField(max_length=20) 
	incognito_last_name= models.CharField(max_length=20) 
	incognito_first_name= models.CharField(max_length=20)
	incognito_father_name= models.CharField(max_length=20)
	incognito_mother_name= models.CharField(max_length=20)
	incognito_birthday_name= models.CharField(max_length=20)
	incognito_birth_quarter= models.CharField(max_length=20)
	incognito_birth_zone= models.CharField(max_length=20) 
	incognito_birth_province= models.CharField(max_length=20) 
	incognito_nationality= models.CharField(max_length=20) 
	incognito_marital_statute= models.CharField(max_length=20) 
	incognito_marital_CNI= models.CharField(max_length=20)

	def __str__(self):
		return f"{ self.incognito_last_name } -- {self.incognito_first_name}"

