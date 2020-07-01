from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from apps.base.models import *

class Document(models.Model):
	user = models.ForeignKey(User, related_name="etatcivil_Beneficiaire_EtatCivil", on_delete=models.CASCADE)
	zone = models.ForeignKey(Zone, max_length=64, related_name="etatcivil_Zone_EtatCivil" , on_delete=models.CASCADE)
	residence_quarter = models.ForeignKey(Quarter, related_name="etatcivil_Quartier_EtatCivil" , max_length=64, on_delete=models.CASCADE)
	date = models.DateField(default=timezone.now)
	marital_statut = models.BooleanField(default=False)
	rejection_msg = models.TextField(null=True, blank=True)
	secretary_validated = models.BooleanField(default=False)
	ready = models.BooleanField(default=False)

	def requirements():
		return ["CNI", "Presence Physique"]


	def price(self):
		try:
			return PriceHistory.objects.filter(zone=self.zone).last().total()
		except:
			return 0


class PriceHistory(models.Model):
	date = models.DateField()
	zone = models.ForeignKey(Zone, related_name="etatcivil_etat_civil_price_province", on_delete=models.CASCADE)
	zone_price = models.IntegerField(default=0)
	
	def total(self):
		return self.zone_price