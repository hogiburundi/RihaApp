from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from apps.base.models import *

class Document(models.Model):
	user = models.ForeignKey(User, related_name="id_compl_user", on_delete=models.CASCADE)
	zone = models.ForeignKey(Zone, related_name="id_compl_zone", max_length=64, on_delete=models.CASCADE)
	residence_quarter = models.ForeignKey(Quarter, related_name="id_compl_residence", max_length=64, on_delete=models.CASCADE)
	date = models.DateField(default=timezone.now)
	payment_method = models.CharField(max_length=64)
	payment_serial = models.CharField(max_length=64)
	rejection_msg = models.TextField(null=True, blank=True)
	secretary_validated = models.BooleanField(default=False)
	ready = models.BooleanField(default=False)

	def price():
		return {"mairie":500}

	def requirements():
		return ["cahier de menage", ]

class PriceHistory(models.Model):
	date = models.DateField()
	quarter = models.ForeignKey('Quarter', related_name="id_compl_price_quarter", on_delete=models.CASCADE)
	quarter_price = models.IntegerField()
	commune = models.ForeignKey('Commune', related_name="id_compl_price_commune", on_delete=models.CASCADE)
	commmune_price = models.IntegerField()
	province = models.ForeignKey('Province', related_name="id_compl_price_province", on_delete=models.CASCADE)
	province_price = models.IntegerField()
	zone = models.ForeignKey('Zone', related_name="id_compl_price_zone", on_delete=models.CASCADE)
	zone_price = models.IntegerField()