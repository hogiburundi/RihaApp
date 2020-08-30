from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from apps.base.models import *

class Document(models.Model):
	user = models.ForeignKey(User, related_name="banmariage_groom", null=True, on_delete=models.SET_NULL)
	bride = models.ForeignKey(Profile, related_name="banmariage_bride", null=True, on_delete=models.SET_NULL)
	zone = models.ForeignKey(Zone, related_name="banmariage_zone", max_length=64, null=True, on_delete=models.SET_NULL)
	residence_quarter = models.ForeignKey(Quarter, related_name="banmariage_residence", max_length=64, null=True, on_delete=models.SET_NULL)
	date_mariage = models.DateField(default=timezone.now)
	date = models.DateField(default=timezone.now)
	rejection_msg = models.TextField(null=True, blank=True)
	secretary_validated = models.BooleanField(default=False, null=True, blank=True)
	ready = models.BooleanField(default=False)
	zone_payment = models.ForeignKey(PaymentZone, related_name="banmariage_province_payment", blank=True, null=True, on_delete=models.SET_NULL)



	def requirements():
		return ["CNI(complet)","attestation de celibat","extrait d'etat civil", ]

	def price():
		try:
			return PriceHistory.objects.filter(zone=self.zone).last().total()
		except:
			return 0

	def save(self, *args, **kwargs):
		super(Document, self).save(*args, **kwargs)
		if self.ready:
			Notification(self.user, f"L'attestation de publication des bans de mariage que vous avez demandé le {self.date} à {self.zone} est disponible").save()

	def paymentPercent(self):
		return 100 if self.zone_payment else 0

	def validationPercent(self):
		progression = 0
		progression += 70 if self.secretary_validated != None else 0
		progression += 30 if self.ready else 0
		return progression

	def __str__(self):
		return f"{self.user} {self.zone}"

	def onlyPaid(): # /!\ sans self
		return Document.objects.filter(zone_payment__isnull = False, secretary_validated__isnull=True)
		# tout les filter necessaire en fait pas seulement zone
		# si il y a pas de payments requises : return Document.objects.all()


class PriceHistory(models.Model):
	date = models.DateField()
	zone = models.ForeignKey(Zone, related_name="banmariage_price_province", on_delete=models.CASCADE)
	zone_price = models.IntegerField(default=0)
	
	def total(self):
		return self.zone_price
