from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from apps.base.models import *

class Document(models.Model):
	user = models.ForeignKey(User, related_name='naitdom_BeneficiareNaD', on_delete=models.CASCADE)
	zone = models.ForeignKey(Zone, max_length=64, related_name='naitdom_ZoneNaD', on_delete=models.CASCADE)
	residence_quarter = models.ForeignKey(Quarter, related_name='naitdom_QuartierNaD', on_delete=models.CASCADE)
	date = models.DateField(default=timezone.now)
	child_name = models.CharField(max_length=50)
	child_birth = models.DateField()
	child_birth_zone = models.ForeignKey(Zone, related_name='naitdom_ChildBirthZoneNaD', on_delete=models.CASCADE)
	child_birth_quarter = models.ForeignKey(Quarter, related_name='naitdom_ChildBirthQuarterNaD', on_delete=models.CASCADE)
	child_mother = models.ForeignKey(Profile, related_name='naitdom_ChildMotherNaD',max_length=64, on_delete=models.CASCADE)
	first_witness = models.ForeignKey(Profile, related_name='naitdom_WitnessNaDO',max_length=64, on_delete=models.CASCADE)
	second_witness = models.ForeignKey(Profile, related_name='naitdom_WitnessNaDT',max_length=64, on_delete=models.CASCADE)
	supervisor = models.ForeignKey(Profile, related_name='naitdom_SupervisorNaD',max_length=64, on_delete=models.CASCADE)
	rejection_msg = models.TextField(null=True, blank=True)
	secretary_validated = models.BooleanField(default=False)
	ready = models.BooleanField(default=False)

	def price(self):
		try:
			return PriceHistory.objects.filter(zone=self.zone).last().total()
		except:
			return 0

	def requirements():
		return ["presence et CNI du declarant","presence et CNI de deux temoins",]


class PriceHistory(models.Model):
	date = models.DateField()
	zone = models.ForeignKey(Zone, related_name="naitdom_price_province", on_delete=models.CASCADE)
	zone_price = models.IntegerField(default=0)
	
	def total(self):
		return self.zone_price