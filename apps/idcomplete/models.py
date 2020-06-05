from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from apps.base.models import *

class Document(models.Model):
	user = models.ForeignKey(User, related_name="id_compl_user", on_delete=models.CASCADE)
	zone = models.ForeignKey(Zone, related_name="id_compl_zone", max_length=64, on_delete=models.CASCADE)
	residence_quarter = models.ForeignKey(Quarter, related_name="id_compl_residence", max_length=64, on_delete=models.CASCADE)
	date = models.DateField(default=timezone.now)
	rejection_msg = models.TextField(null=True, blank=True)
	secretary_validated = models.BooleanField(default=False)
	ready = models.BooleanField(default=False)
	price = models.ForeignKey("PriceHistory", null=True, on_delete=models.SET_NULL)

	def requirements():
		return ["cahier de menage", ]

class PriceHistory(models.Model):
	date = models.DateField()
	quarter = models.ForeignKey(Quarter, related_name="id_compl_price_quarter", on_delete=models.CASCADE)
	quarter_price = models.IntegerField(default=0)
	commune = models.ForeignKey(Commune, related_name="id_compl_price_commune", on_delete=models.CASCADE)
	commmune_price = models.IntegerField(default=0)
	province = models.ForeignKey(Province, related_name="id_compl_price_province", on_delete=models.CASCADE)
	province_price = models.IntegerField(default=0)
	zone = models.ForeignKey(Zone, related_name="id_compl_price_zone", on_delete=models.CASCADE)
	zone_price = models.IntegerField(default=0)

	def total(self):
		return self.quarter_price+self.commmune_price+self.zone_price+self.province_price