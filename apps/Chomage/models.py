from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from apps.base.models import *



class Document(models.Model):
	user                = models.ForeignKey(User, related_name="chomage_user", null=True, on_delete=models.SET_NULL)
	zone                = models.ForeignKey(Zone, related_name="chomage_zone", max_length=64, null=True, on_delete=models.SET_NULL)
	residence_quarter   = models.ForeignKey(Quarter, related_name="chomage_residence", max_length=64, null=True, on_delete=models.SET_NULL)
	date_delivrated     = models.DateField(default=timezone.now)
	anneeEnChomage      = models.IntegerField()
	rejection_msg       = models.TextField(null=True, blank=True)
	secretary_validated = models.BooleanField(null=True)
	ready               = models.BooleanField(default=False)
	zone_payment        = models.ForeignKey(PaymentZone, related_name="chomage_province_payment", blank=True, null=True, on_delete=models.SET_NULL)

	def __str__(self):
		return '{} {}'.format(self.user.last_name, self.user.first_name)
	
	def requirements():
		return ["presence physique ou autre document prouvant son existance" ]
	def save(self, *args, **kwargs):
		super(Document, self).save(*args, **kwargs)
		if self.ready:
			Notification(self.user, f"l'attestation de chomage que vous avez demandé le {self.date_delivrated} à {self.zone} est disponible").save()

	def price(self):
		try:
			return PriceHistory.objects.filter(zone=self.zone).last().total()
		except:
			return 500
	def onlyPaid():
		return Document.objects.filter(zone_payment=True)

	def paymentPercent(self):
		return 100 if self.zone_payment else 0

	def validationPercent(self):
		return 100 if self.secretary_validated != None else 0



class PriceHistory(models.Model):
	date = models.DateField()
	zone = models.ForeignKey(Zone, related_name="chomage_price_province", on_delete=models.CASCADE)
	zone_price = models.IntegerField(default=0)
	
	def total(self):
		return self.zone_price