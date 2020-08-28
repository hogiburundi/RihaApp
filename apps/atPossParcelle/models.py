from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from apps.base.models import *

class Document(models.Model):
	user = models.ForeignKey(User, related_name="atposs_parc_user", null=True, on_delete=models.SET_NULL)
	zone = models.ForeignKey(Zone, related_name="atposs_parc_zone", max_length=64, null=True, on_delete=models.SET_NULL)
	residence_quarter = models.ForeignKey(Quarter, related_name="atposs_residence_user", max_length=64, null=True, on_delete=models.SET_NULL)
	quarter_propriety = models.ForeignKey(Quarter, related_name="atposs_parc_residence", max_length=64, null=True, on_delete=models.SET_NULL)
	propriety_surface = models.FloatField(null=True, blank=True)
	date = models.DateField(default=timezone.now)
	rejection_msg = models.TextField(null=True, blank=True)
	secretary_validated = models.BooleanField(default=False,null=True)
	ready = models.BooleanField(default=False)
	zone_payment = models.ForeignKey(PaymentZone, related_name="atposs_parc_province_payment", blank=True, null=True, on_delete=models.SET_NULL)

	def requirements():
		return ["cahier de menage", "CNI", "presence des papiers de ladite parcelle"]

	def price():
		try:
			return PriceHistory.objects.filter(zone=self.zone).last().total()
		except:
			return 0

	def save(self, *args, **kwargs):
		super(Document, self).save(*args, **kwargs)
		if self.ready:
			Notification(self.user, f"l'identité complete que vous avez demandé le {self.date} à {self.zone} est disponible").save()

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
	zone = models.ForeignKey(Zone, related_name="atposs_price_province", on_delete=models.CASCADE)
	zone_price = models.IntegerField(default=0)
	
	def total(self):
		return self.zone_price



