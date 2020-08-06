from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from apps.base.models import *
from apps.base.date_conversion import lireDate


class Document(models.Model):
	user = models.ForeignKey(User, related_name="notoriete_user", null=True, on_delete=models.SET_NULL)
	date = models.DateField(default=timezone.now)
	comparant_1 = models.ForeignKey(Profile, related_name="notoriete_comparant_1", on_delete=models.CASCADE)
	comparant_2 = models.ForeignKey(Profile, related_name="notoriete_comparant_2", null=True, on_delete=models.SET_NULL)
	comparant_3 = models.ForeignKey(Profile, related_name="notoriete_comparant_3", null=True, on_delete=models.SET_NULL)

	zone = models.ForeignKey(Zone, related_name="notoriete_zone", max_length=64, null=True, on_delete=models.SET_NULL)
	rejection_msg = models.TextField(null=True, blank=True)
	secretary_validated = models.BooleanField(null=True)
	ready = models.BooleanField(default=False)
	zone_payment = models.ForeignKey(PaymentZone, related_name="notoriete_province_payment", blank=True, null=True, on_delete=models.SET_NULL)

	def __str__(self):
		return '{} {}'.format(self.user.last_name, self.user.first_name)
	
	def requirements():
		return ["CNI", "presence physique ou autre document prouvant son existance" ]
				
	def save(self, *args, **kwargs):
		super(Document, self).save(*args, **kwargs)
		if self.ready:
			Notification(self.user, f"l'attestation de notoriete que vous avez demandé le {self.date_delivrated} à {self.zone} est disponible").save()

	def price(self):
		try:
			return PriceHistory.objects.filter(zone=self.zone).last().total()
		except:
			return 10000

	def payment_percent(self):
		return 100 if self.zone_payment else 0

	def validation_percent(self):
		return 100 if self.secretary_validated != None else 0

	def onlyPaid():
		return Document.objects.filter(zone_payment=True)

	def dateString(self):
		return lireDate(self.date)

class PriceHistory(models.Model):
	date = models.DateField()
	zone = models.ForeignKey(Zone, related_name="notoriete_price_province", on_delete=models.CASCADE)
	zone_price = models.IntegerField(default=0)
	
	def total(self):
		return self.zone_price