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
	zone_payment = models.ForeignKey(PaymentZone, related_name="recom_province_payment", blank=True, null=True, on_delete=models.SET_NULL)
	ready = models.BooleanField(default=False)


	def requirements():
		return ["copie de contrat d'execution d'un travail quelconque", ]

	def price(self):
		try:
			return PriceHistory.objects.filter(zone=self.zone).last().total()
		except:
			return 0

	def save(self, *args, **kwargs):
		super(Document, self).save(*args, **kwargs)
		if self.ready:
			Notification(self.user, f"l'identité complete que vous avez demandé le {self.date} à {self.zone} est disponible").save()

	def payment_percent(self):
		return 100 if self.zone_payment else 0

	def validation_percent(self):
		return 100 if self.secretary_validated  else 0

	def __str__(self):
		return f"{self.user} {self.zone}"

	def onlyPaid(): # /!\ sans self
		return Document.objects.filter(zone_payment=True)
		# tout les filter necessaire en fait pas seulement zone
		# si il y a pas de payments requises : return Document.objects.all()


class PriceHistory(models.Model):
	date = models.DateField()
	zone = models.ForeignKey(Zone, related_name="recom_price_province", on_delete=models.CASCADE)
	zone_price = models.IntegerField(default=0)
	
	def total(self):
		return self.zone_price