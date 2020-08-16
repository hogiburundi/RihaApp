from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from apps.base.models import *

class Document(models.Model):
	user = models.ForeignKey(User, related_name="at_app_parc_user", null=True, on_delete=models.SET_NULL)
	user_residence_quarter = models.ForeignKey(Quarter, related_name="at_app_parc_residence_quarter_user", max_length=64, null=True, on_delete=models.SET_NULL)
	propriety_quarter = models.ForeignKey(Quarter, related_name="at_app_parc_propr", max_length=64, null=True, on_delete=models.SET_NULL)
	propriety_surfaces_a = models.FloatField(null=True, blank=True)
	propriety_surfaces_ca = models.FloatField(null=True, blank=True)
	date = models.DateField(default=timezone.now)
	propriety_contenency = models.CharField(max_length=100)
	rejection_msg = models.TextField(null=True, blank=True)
	secretary_validated = models.BooleanField(default=False, null=True, blank=True)
	ready = models.BooleanField(default=False)
	zone_payment = models.ForeignKey(PaymentZone, related_name="at_app_parc_province_payment", blank=True, null=True, on_delete=models.SET_NULL)

	def requirements():
		return ["cahier de menage", "CNI", "papiers de ladite parcelle"]

	def price(self):
		try:
			return PriceHistory.objects.filter(zone=self.propriety_quarter.zone).last().total()
		except:
			return 0

	def save(self, *args, **kwargs):
		super(Document, self).save(*args, **kwargs)
		if self.ready:
			Notification(self.user, f"l'attestation d'appartenance de parcelle que vous avez demandé le {self.date} à {self.zone} est disponible").save()

	def paymentPercent(self):
		return 100 if self.zone_payment else 0

	def onlyPaid():
		return Document.objects.filter(zone_payment__isnull=False, secretary_validated__isnull=True)

	def validationPercent(self):
		progression = 0
		progression += 70 if self.secretary_validated != None else 0
		progression += 30 if self.ready else 0
		return progression

	def __str__(self):
		return f"{self.user} {self.zone}"
		# tout les filter necessaire en fait pas seulement zone
		# si il y a pas de payments requises : return Document.objects.all()


class PriceHistory(models.Model):
	date = models.DateField()
	zone = models.ForeignKey(Zone, related_name="at_app_parc_price_province", on_delete=models.CASCADE)
	zone_price = models.IntegerField(default=0)
	
	def total(self):
		return self.zone_price



