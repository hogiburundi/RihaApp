from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from apps.base.models import *
from apps.base.date_conversion import lireDate

class Document(models.Model):
	user = models.ForeignKey(User, related_name="vente_user", null=True, on_delete=models.SET_NULL)
	date = models.DateField(default=timezone.now)
	rejection_msg = models.TextField(null=True, blank=True)
	secretary_validated = models.BooleanField(null=True)
	ready = models.BooleanField(default=False)
	zone_payment = models.ForeignKey(PaymentZone, related_name="vente_province_payment", blank=True, null=True, on_delete=models.SET_NULL)
	amount = models.CharField(max_length=64,null=True)
	buyer = models.ForeignKey(Profile, related_name="vente_buyer", null=True, on_delete=models.SET_NULL)
	property_quarter = models.ForeignKey(Quarter, related_name="property_quarter", max_length=64, null=True, on_delete=models.SET_NULL)
	witness11 = models.ForeignKey(Profile, related_name="vente_witness11", null=True, on_delete=models.SET_NULL)
	witness12 = models.ForeignKey(Profile, related_name="vente_witness12", null=True, on_delete=models.SET_NULL)
	witness21 = models.ForeignKey(Profile, related_name="vente_witness21", null=True, on_delete=models.SET_NULL)
	witness22 = models.ForeignKey(Profile, related_name="vente_witness22", null=True, on_delete=models.SET_NULL)
	deleted = models.BooleanField(default=False)

	def requirements():
		return ["cahier de menage", "CNI"]

	def save(self, *args, **kwargs):
		super(Document, self).save(*args, **kwargs)
		if self.ready:
			Notification(self.user, f"l'identité complete que vous avez demandé le {self.date} à {self.property_quarter.zone} est disponible").save()

	def price():
		try:
			return PriceHistory.objects.filter(zone=self.zone).last().total()
		except:
			return 0

	def paymentPercent(self):
		return 100 if self.zone_payment else 0

	def onlyPaid():
		return Document.objects.filter(zone_payment__isnull=False, secretary_validated__isnull=True)

		
	def validationPercent(self):
		return 100 if self.secretary_validated != None else 0

	def __str__(self):
		return f"{self.user} {self.property_quarter.zone}"

class PriceHistory(models.Model):
	date = models.DateField()
	zone = models.ForeignKey(Zone, related_name="vente_price_province", on_delete=models.CASCADE)
	zone_price = models.IntegerField(default=0)
	
	def total(self):
		return self.zone_price