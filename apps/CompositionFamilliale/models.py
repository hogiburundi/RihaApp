from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from apps.base.models import *



class Document(models.Model):
	name_apps          = models.CharField(max_length = 50, default = "Attestation de composition familliale")
	user = models.ForeignKey(User, related_name="composition_user", null=True, on_delete=models.SET_NULL)
	fullname_lady      = models.CharField(max_length = 50) 
	zone = models.ForeignKey(Zone, related_name="composition_zone", max_length=64, null=True, on_delete=models.SET_NULL)
	residence_quarter = models.ForeignKey(Quarter, related_name="composition_residence", max_length=64, null=True, on_delete=models.SET_NULL)
	# date = models.DateField(default=timezone.now)
	date_delivrated    = models.DateField(default=timezone.now)
	rejection_msg = models.TextField(null=True, blank=True)
	secretary_validated = models.BooleanField(null=True)
	ready = models.BooleanField(default=False)
	zone_payment = models.ForeignKey(PaymentZone, related_name="composition_province_payment", blank=True, null=True, on_delete=models.SET_NULL)

	def __str__(self):
		return '{} {}'.format(self.user.last_name, self.user.first_name)
	
	def requirements():
		return ["CNI",
				"presence physique ou autre document prouvant son existance" ]
	def save(self, *args, **kwargs):
		super(Document, self).save(*args, **kwargs)
		if self.ready:
			Notification(self.user, f"l'attestation de composition familliiale que vous avez demandé le {self.date_delivrated} à {self.zone} est disponible").save()

	def price(self):
		try:
			return PriceHistory.objects.filter(zone=self.zone).last().total()
		except:
			return 500

	def payment_percent(self):
		return 100 if self.zone_payment else 0

	def validation_percent(self):
		return 100 if self.secretary_validated != None else 0



	def get_child(self):
		return ', '.join(self.fullname_child.all().values_list('fullname_child', flat=True))


class PriceHistory(models.Model):
	date = models.DateField()
	zone = models.ForeignKey(Zone, related_name="composition_price_province", on_delete=models.CASCADE)
	zone_price = models.IntegerField(default=0)
	
	def total(self):
		return self.zone_price






class Child(models.Model):
	document       = models.ForeignKey(Document, on_delete = models.CASCADE)
	fullname_child = models.CharField(max_length = 50)
	age            = models.CharField(max_length = 50)

	def __str__(self):
		return self.fullname_child