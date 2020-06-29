from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from apps.base.models import *


class Document(models.Model):
	name_apps          = models.CharField(max_length = 50, default = "Attestation de marriage")
	user = models.ForeignKey(User, related_name="marriage_user", null=True, on_delete=models.SET_NULL)
	

	age_epoux         = models.CharField(max_length = 100)
	year              = models.CharField(max_length = 100)#for the user en lettres
	jour              = models.CharField(max_length = 100)
	mois              = models.CharField(max_length = 100)
	
	nom_prenom_epouse= models.CharField(max_length = 100)
	nom_prenom_pere_epouse  = models.CharField(max_length = 100)
	nom_prenom_mere_epouse  = models.CharField(max_length = 100)
	age_epouse              = models.CharField(max_length = 100)
	job_epouse         = models.CharField(max_length = 100)
	residence_epouse   = models.CharField(max_length = 100)
	nationalite_epouse = models.CharField(max_length = 100, default = "Burundaise")
	
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

	def validation_percent(self):
		return 100 if self.secretary_validated != None else 0



class PriceHistory(models.Model):
	date = models.DateField()
	zone = models.ForeignKey(Zone, related_name="marriage_price_province", on_delete=models.CASCADE)
	zone_price = models.IntegerField(default=0)
	
	def total(self):
		return self.zone_price