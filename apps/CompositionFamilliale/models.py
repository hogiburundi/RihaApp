from django.db import models
from django.db.models import Q
from django.utils import timezone
from django.contrib.auth.models import User
from apps.base.models import *

class Document(models.Model):
	user = models.ForeignKey(User, related_name="composition_user", null=True, on_delete=models.SET_NULL)
	conjoint = models.ForeignKey(Profile,on_delete = models.PROTECT, related_name = 'conjoint') 
	quarter = models.ForeignKey(Quarter, related_name="composition_zone", max_length=64, null=True, on_delete=models.SET_NULL)
	date = models.DateField(default=timezone.now)
	rejection_msg = models.TextField(null=True, blank=True)
	secretary_validated = models.BooleanField(null=True)
	ready = models.BooleanField(default=False)
	zone_payment = models.ForeignKey(PaymentZone, related_name="composition_province_payment", blank=True, null=True, on_delete=models.SET_NULL)
	
	def __str__(self):
		return '{} {}'.format(self.user.last_name, self.user.first_name)

	def children(self):
		return Child.objects.filter(Q(father=self.user.profile) | Q(mother=self.user.profile))
	
	def requirements():
		return ["CNI", "presence physique ou autre document prouvant son existance" ]
		
	def price(self):
		try:
			return PriceHistory.objects.filter(zone=self.zone).last().total()
		except:
			return 500

	def payment_percent(self):
		return 100 if self.zone_payment else 0

	def validation_percent(self):
		return 100 if self.secretary_validated != None else 0


class PriceHistory(models.Model):
	date = models.DateField()
	zone = models.ForeignKey(Zone, related_name="composition_price_province", on_delete=models.CASCADE)
	zone_price = models.IntegerField(default=0)
	
	def total(self):
		return self.zone_price

class Child(models.Model):
	father = models.ForeignKey(Profile, on_delete = models.PROTECT, related_name = 'composition_father')
	mother = models.ForeignKey(Profile, on_delete = models.PROTECT, related_name = 'composition_mother')
	name = models.CharField(max_length = 50)
	date = models.DateField()

	class Meta:
		unique_together = ('father', 'mother', 'name', 'date')

	def __str__(self):
		return self.name

	def childrenOf(user):
		return Child.objects.filter(Q(father=user) | Q(mother=user))