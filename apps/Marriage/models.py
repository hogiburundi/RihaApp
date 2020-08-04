from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from apps.base.models import *
from apps.base.date_conversion import lireDate
import inflect


class Document(models.Model):
	name_apps          = models.CharField(max_length = 50, default = "Attestation de marriage")
	user = models.ForeignKey(User, related_name="marriage_user", null=True, on_delete=models.SET_NULL)
	


	conjoint = models.ForeignKey(Profile, related_name="epoux_epouse", null=True, on_delete=models.SET_NULL)
	acte  = models.IntegerField()
	volume = models.IntegerField()
	date  = models.DateField(default=timezone.now)

	
	
	zone = models.ForeignKey(Zone, related_name="marriage_zone", max_length=64, null=True, on_delete=models.SET_NULL)
	residence_quarter = models.ForeignKey(Quarter, related_name="marriage_residence", max_length=64, null=True, on_delete=models.SET_NULL)
	date_delivrated    = models.DateField(default=timezone.now)
	rejection_msg = models.TextField(null=True, blank=True)
	secretary_validated = models.BooleanField(null=True)
	ready = models.BooleanField(default=False)
	zone_payment = models.ForeignKey(PaymentZone, related_name="marriage_province_payment", blank=True, null=True, on_delete=models.SET_NULL)

	def __str__(self):
		return '{} {}'.format(self.user.last_name, self.user.first_name)
	
	def requirements():
		return ['numero d\'acte']

	def save(self, *args, **kwargs):
		super(Document, self).save(*args, **kwargs)
		if self.ready:
			Notification(self.user, f"l'attestation de marriage que vous avez demandé le {self.date_delivrated} à {self.zone} est disponible").save()

	def price(self):
		try:
			return PriceHistory.objects.filter(zone=self.zone).last().total()
		except:
			return 1000

	def payment_percent(self):
		return 100 if self.zone_payment else 0


	def onlyPaid():
		return Document.objects.filter(zone_payment=True)

	def validation_percent(self):
		return 100 if self.secretary_validated != None else 0

	def __str__(self):
		return f"{self.user} {self.zone}"


	def dateString(self):
		return lireDate(self.date)

	def ageString(self):
		p = inflect.engine()
		return p.number_to_words(self.date)




class PriceHistory(models.Model):
	date = models.DateField()
	zone = models.ForeignKey(Zone, related_name="marriage_price_province", on_delete=models.CASCADE)
	zone_price = models.IntegerField(default=0)
	
	def total(self):
		return self.zone_price