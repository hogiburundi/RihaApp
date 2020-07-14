from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from apps.base.models import *

class Document(models.Model):
	user = models.ForeignKey(User, related_name='recom_Beneficiare', on_delete=models.CASCADE)
	zone = models.ForeignKey(Zone, max_length=64, related_name='recom_Zone', on_delete=models.CASCADE)
	residence_quarter = models.ForeignKey(Quarter, related_name='recom_Quartier', max_length=64, on_delete=models.CASCADE)
	date = models.DateField(default=timezone.now)
	payment_method = models.CharField(max_length=64)
	payment_serial = models.CharField(max_length=64)
	rejection_msg = models.TextField(null=True, blank=True)
	secretary_validated = models.BooleanField(default=False)
	ready = models.BooleanField(default=False)


	def requirements():
		return ["copie de contrat d'execution d'un travail quelconque", ]

	def price(self):
		try:
			return PriceHistory.objects.filter(zone=self.zone).last().total()
		except:
			return 0


class PriceHistory(models.Model):
	date = models.DateField()
	zone = models.ForeignKey(Zone, related_name="recom_price_province", on_delete=models.CASCADE)
	zone_price = models.IntegerField(default=0)
	
	def total(self):
		return self.zone_price