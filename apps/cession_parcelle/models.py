from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from apps.base.models import *

class Document(models.Model):
	user = models.ForeignKey(User, related_name="cession_user", null=True, on_delete=models.SET_NULL)
	zone = models.ForeignKey(Zone, related_name="cession_zone", max_length=64, null=True, on_delete=models.SET_NULL)
	residence_quarter = models.ForeignKey(Quarter, related_name="cession_residence", max_length=64, null=True, on_delete=models.SET_NULL)
	date = models.DateField(default=timezone.now)
	rejection_msg = models.TextField(null=True, blank=True)
	secretary_validated = models.BooleanField(null=True)
	ready = models.BooleanField(default=False)
	zone_payment = models.ForeignKey(PaymentZone, related_name="cession_province_payment", blank=True, null=True, on_delete=models.SET_NULL)
	mrs = models.CharField(max_length=100, null=True)
	realestate_quarter = models.ForeignKey(Quarter, related_name="cession_quarterr", max_length=64, null=True, on_delete=models.SET_NULL)
	beneficiary = models.CharField(max_length=100, null=True)
	beneficiary_zone = models.ForeignKey(Zone, related_name="cession_zonee", max_length=64, null=True, on_delete=models.SET_NULL)
	beneficiary_residence_zone = models.ForeignKey(Zone, related_name="cession_res_zone", max_length=64, null=True, on_delete=models.SET_NULL)
	beneficiary_residence_quarter = models.ForeignKey(Quarter, related_name="cession_res_qu", max_length=64, null=True, on_delete=models.SET_NULL)
	giv_eyewitness1 = models.CharField(max_length=100, null=True)
	giv_eyewitness2 = models.CharField(max_length=100, null=True)
	ben_eyewitness1 = models.CharField(max_length=100, null=True)
	ben_eyewitness2 = models.CharField(max_length=100, null=True)

	def requirements():
		return ["cahier de menage", "CNI"]

	def save(self, *args, **kwargs):
		super(Document, self).save(*args, **kwargs)
		if self.ready:
			Notification(self.user, f"l'identité complete que vous avez demandé le {self.date} à {self.zone} est disponible").save()

	def price(self):
		try:
			return PriceHistory.objects.filter(zone=self.zone).last().total()
		except:
			return 0

	def payment_percent(self):
		return 100 if self.zone_payment else 0

	def validation_percent(self):
		return 100 if self.secretary_validated != None else 0

	def __str__(self):
		return f"{self.user} {self.zone}"

class PriceHistory(models.Model):
	date = models.DateField()
	zone = models.ForeignKey(Zone, related_name="cession_price_province", on_delete=models.CASCADE)
	zone_price = models.IntegerField(default=0)
	
	def total(self):
		return self.zone_price