from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from apps.base.models import *

#------------		DM = DEAD MEAN 		---------------------#

class Document(models.Model):
	user = models.ForeignKey(User, related_name='at_deces_dom_declarant', on_delete=models.CASCADE)
	zone = models.ForeignKey(Zone, max_length=64, related_name='ZoneNaD', on_delete=models.CASCADE)

	dead_man = models.ForeignKey(User, related_name='at_deces_dom_defunt', on_delete=models.CASCADE)
	residence_quarter_DM = models.ForeignKey(Quarter, related_name='at_deces_dom_quartier_resi_defunt', on_delete=models.CASCADE)

	DM_date = models.DateField(default=timezone.now, verbose_name='at_deces_dom_date_deces')

	first_witness = models.ForeignKey(Profile, related_name='at_deces_dom_T1',max_length=64, on_delete=models.CASCADE)
	second_witness = models.ForeignKey(Profile, related_name='at_deces_dom_T2',max_length=64, on_delete=models.CASCADE)

	quarter_leader = models.ForeignKey(Profile, related_name='at_deces_dom_quater_leader',max_length=64, on_delete=models.CASCADE)
	rejection_msg = models.TextField(null=True, blank=True)
	secretary_validated = models.BooleanField(default=False)
	ready = models.BooleanField(default=False)

	def price(self):
		try:
			return PriceHistory.objects.filter(zone=self.zone).last().total()
		except:
			return 0

	def requirements():
		return ["presence  physique et CNI du declarant","presence et CNI de deux temoins",]


class DocumentManualy(models.Model):
	user = models.ForeignKey(User, related_name='at_deces1_dom_declarant', on_delete=models.CASCADE)
	zone = models.ForeignKey(Zone, max_length=64, related_name='at_deces2_dom_zone', on_delete=models.CASCADE)
	dead_man_f_l_name = models.CharField(max_length=50)
	gender = models.TextField(max_length=2)
	DM_mother = models.CharField(max_length=64)
	DM_father = models.CharField(max_length=64)
	DM_origin_quarter = models.ForeignKey(Quarter, related_name='at_deces3_dom_quartier_origine', on_delete=models.CASCADE)
	DM_residence_quarter = models.ForeignKey(Quarter, related_name='at_deces4_dom_quartier_resi_defunt', on_delete=models.CASCADE)
	DM_death_date = models.DateField(default=timezone.now, verbose_name='at_deces5_dom_date_deces')
	first_witness = models.CharField(max_length=60)
	second_witness = models.CharField(max_length=60)
	quarter_leader = models.ForeignKey(Profile, related_name='at_deces6_SupervisorNaD',max_length=64, on_delete=models.CASCADE)
	rejection_msg = models.TextField(null=True, blank=True)
	secretary_validated = models.BooleanField(default=False)
	ready = models.BooleanField(default=False)

	def price(self):
		try:
			return PriceHistory.objects.filter(zone=self.zone).last().total()
		except:
			return 0

	def requirements():
		return ["presence  physique et CNI du declarant","presence et CNI de deux temoins",]


class PriceHistory(models.Model):
	date = models.DateField()
	zone = models.ForeignKey(Zone, related_name="deces9_domicile_price_province", on_delete=models.CASCADE)
	zone_price = models.IntegerField(default=0)
	
	def total(self):
		return self.zone_price