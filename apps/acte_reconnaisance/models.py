from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from apps.base.models import *
from apps.base.date_conversion import lireDate

class Document(models.Model):
	user = models.ForeignKey(User, related_name="act_recon_user", null=True, on_delete=models.SET_NULL)
	zone = models.ForeignKey(Zone, related_name="act_recon_zone", max_length=64, null=True, on_delete=models.SET_NULL)
	residence_quarter = models.ForeignKey(Quarter, related_name="act_recon_residence", max_length=64, null=True, on_delete=models.SET_NULL)
	date = models.DateField(default=timezone.now)
	rejection_msg = models.TextField(null=True, blank=True)
	secretary_validated = models.BooleanField(null=True)
	ready = models.BooleanField(default=False)
	zone_payment = models.ForeignKey(PaymentZone, related_name="act_recon_province_payment", blank=True, null=True, on_delete=models.SET_NULL)
	volume = models.CharField(max_length=64, null=True, blank=True)
	acte = models.CharField(max_length=64, null=True, blank=True)
	witness1 = models.CharField(max_length=64, null=True, blank=True)
	witness2 = models.CharField(max_length=64, null=True, blank=True)
	day_month_year = models.DateField(default=timezone.now)
	work = models.CharField(max_length=64, null=True, blank=True)
	wife = models.CharField(max_length=64, null=True, blank=True)
	wife_age = models.CharField(max_length=64, null=True, blank=True)
	wife_work = models.CharField(max_length=64, null=True, blank=True)
	wife_province = models.CharField(max_length=64, null=True, blank=True)
	witness_work1 = models.CharField(max_length=64, null=True, blank=True)
	witness_work2 = models.CharField(max_length=64, null=True, blank=True)
	witness_province1 = models.CharField(max_length=64, null=True, blank=True)
	witness_province2 = models.CharField(max_length=64, null=True, blank=True)
	witness_age1 = models.CharField(max_length=64, null=True, blank=True)
	witness_age2 = models.CharField(max_length=64, null=True, blank=True)
	child = models.CharField(max_length=64, null=True, blank=True)
	child_province = models.CharField(max_length=64, null=True, blank=True)
	child_date = models.DateField(default=timezone.now)
	child_age = models.CharField(max_length=64, null=True, blank=True)
	witness_nationality1 = models.CharField(max_length=64, null=True, blank=True, default="Burundaise")
	witness_nationality2 = models.CharField(max_length=64, null=True, blank=True, default="Burundaise")
	wife_nationality = models.CharField(max_length=64, null=True, blank=True, default="Burundaise")
	witness_gender1 = models.CharField(max_length=64, null=True, blank=True, default="Homme")
	witness_gender2 = models.CharField(max_length=64, null=True, blank=True, default="Homme")
	child_gender3 = models.CharField(max_length=64, null=True, blank=True, default="Homme")
	wife_gender3 = models.CharField(max_length=64, null=True, blank=True, default="Femme")
	search_place = models.ForeignKey(Quarter, related_name="act_recon_search", max_length=64, null=True, on_delete=models.SET_NULL)

	def requirements():
		return ["cahier de menage", "CNI"]

	def save(self, *args, **kwargs):
		super(Document, self).save(*args, **kwargs)
		if self.ready:
			Notification(self.user, f"l'identité complete que vous avez demandé le {self.date} à {self.zone} est disponible").save()

	def price():
		try:
			return PriceHistory.objects.filter(zone=self.zone).last().total()
		except:
			return 0

	def paymentPercent(self):
		return 100 if self.zone_payment else 0

	def onlyPaid():
		return Document.objects.filter(zone_payment__isnull=False, secretary_validated__isnull=True)


	def dateString(self):
		return lireDate(self.day_month_year)

	def dateString1(self):
		return lireDate(self.child_date)

	def validationPercent(self):
		return 100 if self.secretary_validated != None else 0

	def __str__(self):
		return f"{self.user} {self.zone}"

class PriceHistory(models.Model):
	date = models.DateField()
	zone = models.ForeignKey(Zone, related_name="act_recon_price_province", on_delete=models.CASCADE)
	zone_price = models.IntegerField(default=0)
	
	def total(self):
		return self.zone_price