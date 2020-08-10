from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from apps.base.models import *

class Document(models.Model):
	user = models.ForeignKey(User, related_name="etatcivil_Beneficiaire_EtatCivil",null=True, on_delete=models.SET_NULL)
	zone = models.ForeignKey(Zone, max_length=64, related_name="etatcivil_Zone_EtatCivil" , null=True, on_delete=models.SET_NULL)
	residence_quarter = models.ForeignKey(Quarter, related_name="etatcivil_Quartier_EtatCivil" , null=True, on_delete=models.SET_NULL)
	rejection_msg = models.TextField(null=True, blank=True)
	secretary_validated = models.BooleanField(default=False)
	date = models.DateField(default=timezone.now)
	ready = models.BooleanField(default=False)
	zone_payment = models.ForeignKey(PaymentZone, related_name="etatcivil_province_payment", blank=True, null=True, on_delete=models.SET_NULL)
	

	def requirements():
		return ["CNI", "Presence Physique", "500"]


	def price(self):
		try:
			return PriceHistory.objects.filter(zone=self.zone).last().total()
		except:
			return 0

	def save(self, *args, **kwargs):
		super(Document, self).save(*args, **kwargs)
		if self.ready:
			Notification(self.user, f"Attestation d'état-civil que vous avez demandé le {self.date} à {self.zone} est disponible").save()

	def payment_percent(self):
		return 100 if self.zone_payment else 0

	def validation_percent(self):
		return 100 if self.secretary_validated  else 0

	def __str__(self):
		return f"{self.user} {self.zone}"

	def onlyPaid(): # /!\ sans self
		return Document.objects.filter(zone_payment__isnull = False)
		# tout les filter necessaire en fait pas seulement zone
		# si il y a pas de payments requises : return Document.objects.all()


class PriceHistory(models.Model):
	date = models.DateField()
	zone = models.ForeignKey(Zone, related_name="etatcivil_etat_civil_price_province",null=True, on_delete=models.SET_NULL)
	zone_price = models.IntegerField(default=0)
	
	def total(self):
		return self.zone_price

