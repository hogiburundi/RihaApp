from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from apps.base.models import *

class Document(models.Model):
	user = models.ForeignKey(User, related_name='naitdom_BeneficiareNaD', null=True, on_delete=models.SET_NULL)
	zone = models.ForeignKey(Zone, max_length=64, related_name='naitdom_ZoneNaD', null=True, on_delete=models.SET_NULL)
	residence_quarter = models.ForeignKey(Quarter, related_name='naitdom_QuartierNaD', max_length=64, null=True, on_delete=models.SET_NULL)
	date = models.DateField(default=timezone.now)
	child_name = models.CharField(max_length=50)
	child_birth = models.DateField()
	child_birth_quarter = models.ForeignKey(Quarter, related_name='naitdom_ChildBirthQuarterNaD', null=True, on_delete=models.SET_NULL)
	child_mother = models.ForeignKey(Profile, related_name='naitdom_ChildMotherNaD',max_length=64, null=True, on_delete=models.SET_NULL)
	first_witness = models.ForeignKey(Profile, related_name='naitdom_WitnessNaDO',max_length=64, null=True, on_delete=models.SET_NULL)
	second_witness = models.ForeignKey(Profile, related_name='naitdom_WitnessNaDT',max_length=64, null=True, on_delete=models.SET_NULL)
	rejection_msg = models.TextField(null=True, blank=True)
	secretary_validated = models.BooleanField(default=False, blank=True, null=True)
	ready = models.BooleanField(default=False)
	

	def price(self):
		try:
			return PriceHistory.objects.filter(zone=self.zone).last().total()
		except:
			return 0

	def requirements():
		return ["presence et CNI du declarant","presence et CNI de deux temoins",]

	def save(self, *args, **kwargs):
		super(Document, self).save(*args, **kwargs)
		if self.ready:
			Notification(self.user, f" L'attestation de naissance à domicile  que vous avez demandé le {self.date} à {self.zone} est disponible").save()

# 	def paymentPercent(self):
# 		return 100 if self.zone_payment else 0

# 	def validationPercent(self):
# 		return 100 if self.secretary_validated  else 0

	def __str__(self):
		return f"{self.user} {self.zone}"

# 	# def onlyPaid(): # /!\ sans self
# 	# 	return Document.objects.filter(zone_payment__isnull = False)
# 	# 	# tout les filter necessaire en fait pas seulement zone
# 	# 	# si il y a pas de payments requises : return Document.objects.all()


# class PriceHistory(models.Model):
# 	date = models.DateField()
# 	zone = models.ForeignKey(Zone, related_name="naitdom_price_province", on_delete=models.CASCADE)
# 	zone_price = models.IntegerField(default=0)
	
# 	def total(self):
# 		return self.zone_price