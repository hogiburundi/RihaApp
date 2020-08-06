from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from apps.base.models import *

class Document(models.Model):
	name_apps           = models.CharField(max_length = 50, default = "Attestation d'abandon")
	user                = models.ForeignKey(User, related_name="abandon_user", null=True, on_delete=models.SET_NULL)
	zone                = models.ForeignKey(Zone, related_name="abandon_zone", max_length=64, null=True, on_delete=models.SET_NULL)
	residence_quarter   = models.ForeignKey(Quarter, related_name="abandon_residence", max_length=64, null=True, on_delete=models.SET_NULL)
	
	tuteurAcueillantObjetAbandon  = models.CharField(max_length = 150)
	objet_abandon                 = models.CharField(max_length=50)
	date_delivrated     = models.DateField(default=timezone.now)
	
	rejection_msg       = models.TextField(null=True, blank=True)
	secretary_validated = models.BooleanField(null=True)
	ready               = models.BooleanField(default=False)
	zone_payment        = models.ForeignKey(PaymentZone, related_name="abandon_province_payment", blank=True, null=True, on_delete=models.SET_NULL)

	def __str__(self):
		return '{}'.format(self.objet_abandon)
	
	def requirements():
		return ["CNI",
				"presence physique ou autre document prouvant son existance" ]
	
	def save(self, *args, **kwargs):
		super(Document, self).save(*args, **kwargs)
		if self.ready:
			Notification(self.user, f"l'attestation d'abandon que vous avez demandé le {self.date} à {self.zone} est disponible").save()


	def price(self):
		try:
			return PriceHistory.objects.filter(zone=self.zone).last().total()
		except:
			return 0

	def payment_percent(self):
		return 100 if self.zone_payment else 0

	def onlyPaid():
		return Document.objects.filter(zone_payment=True)

	def validation_percent(self):
		return 100 if self.secretary_validated != None else 0

	def __str__(self):
		return f"{self.user} {self.zone}"



class PriceHistory(models.Model):
	date = models.DateField()
	zone = models.ForeignKey(Zone, related_name="abandon_price_province", on_delete=models.CASCADE)
	zone_price = models.IntegerField(default=0)
	
	def total(self):
		return self.zone_price


