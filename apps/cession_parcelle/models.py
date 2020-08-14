from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from apps.base.models import *
from apps.base.date_conversion import lireDate

class Document(models.Model):
	user = models.ForeignKey(User, related_name="cession_user", null=True, on_delete=models.SET_NULL)
	zone = models.ForeignKey(Zone, related_name="cession_zone", max_length=64, null=True, on_delete=models.SET_NULL)
	residence_quarter = models.ForeignKey(Quarter, related_name="cession_residence", max_length=64, null=True, on_delete=models.SET_NULL)
	date = models.DateField(default=timezone.now)
	rejection_msg = models.TextField(null=True, blank=True)
	secretary_validated = models.BooleanField(null=True)
	ready = models.BooleanField(default=False)
	zone_payment = models.ForeignKey(PaymentZone, related_name="cession_province_payment", blank=True, null=True, on_delete=models.SET_NULL)
	mrs = models.CharField(max_length=64, null=True)
	
	# beneficiary = models.ForeignKey(Profile, related_name="cession_beneficiary", null=True, on_delete=models.SET_NULL)
	beneficiary = models.CharField(max_length=64, null=True, blank=True)
	
	beneficiary_father = models.CharField(max_length=64,null=True)
	beneficiary_mother = models.CharField(max_length=64,null=True)
	beneficiary_residence_zone = models.ForeignKey(Zone, related_name="cession_res_zone", max_length=64, null=True, on_delete=models.SET_NULL)
	beneficiary_residence_quarter = models.ForeignKey(Quarter, related_name="cession_res", max_length=64, null=True, on_delete=models.SET_NULL)
	property_quarter = models.ForeignKey(Quarter, related_name="cession_property_quarter", max_length=64, null=True, on_delete=models.SET_NULL)
	witness11 = models.CharField(max_length=64, null=True, blank=True)
	witness12 = models.CharField(max_length=64, null=True, blank=True)
	witness21 = models.CharField(max_length=64, null=True, blank=True)
	witness22 = models.CharField(max_length=64, null=True, blank=True)
	cnis11 = models.CharField(max_length=64, null=True, blank=True)
	cnis12 = models.CharField(max_length=64, null=True, blank=True)
	cnis21 = models.CharField(max_length=64, null=True, blank=True)
	cnis22 = models.CharField(max_length=64, null=True, blank=True)
	giver_witness_residence1 = models.CharField(max_length=64, null=True, blank=True)
	giver_witness_residence2 = models.CharField(max_length=64, null=True, blank=True)
	benficiary_witness_residence1 = models.CharField(max_length=64, null=True, blank=True)
	benficiary_witness_residence2 = models.CharField(max_length=64, null=True, blank=True)
	search_place = models.ForeignKey(Quarter, related_name="cession_search", max_length=64, null=True, on_delete=models.SET_NULL)


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

	def onlyPaid():
		return Document.objects.filter(zone_payment__isnull=False, secretary_validated__isnull=True)


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