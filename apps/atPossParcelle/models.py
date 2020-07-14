from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from apps.base.models import *

class Document(models.Model):
	user = models.ForeignKey(User, related_name="atposs_parc_user", null=True, on_delete=models.SET_NULL)
	zone = models.ForeignKey(Zone, related_name="atposs_parc_zone", max_length=64, null=True, on_delete=models.SET_NULL)
	residence_quarter = models.ForeignKey(Quarter, related_name="atposs_parc_residence", max_length=64, null=True, on_delete=models.SET_NULL)
	date = models.DateField(default=timezone.now)
	first_witness = models.ForeignKey(User, related_name='atposs_parc_witness1',max_length=64, on_delete=models.CASCADE)
	second_witness = models.ForeignKey(User, related_name='atposs_parc_witness2',max_length=64, on_delete=models.CASCADE)
	quarter_leader = models.ForeignKey(User, related_name='atposs_parc_quater_leader',max_length=64, on_delete=models.CASCADE)
	rejection_msg = models.TextField(null=True, blank=True)
	secretary_validated = models.BooleanField(null=True)
	ready = models.BooleanField(default=False)
	zone_payment = models.ForeignKey(PaymentZone, related_name="atposs_parc_province_payment", blank=True, null=True, on_delete=models.SET_NULL)

	def requirements():
		return ["cahier de menage", "CNI"]

	def price(self):
		try:
			return PriceHistory.objects.filter(zone=self.zone).last().total()
		except:
			return 0


class PriceHistory(models.Model):
	date = models.DateField()
	zone = models.ForeignKey(Zone, related_name="atposs_price_province", on_delete=models.CASCADE)
	zone_price = models.IntegerField(default=0)
	
	def total(self):
		return self.zone_price



