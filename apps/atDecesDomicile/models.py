from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from apps.base.models import *

class Document(models.Model):
	user = models.ForeignKey(User, related_name='at_deces_dom_declarant', on_delete=models.CASCADE)
	zone = models.ForeignKey(Zone, max_length=64, related_name='ZoneNaD', on_delete=models.CASCADE)

	dead_man = models.ForeignKey(Profile, related_name='at_deces_dom_defunt', on_delete=models.CASCADE)
	residence_quarter_DM = models.ForeignKey(Quarter, related_name='at_deces_dom_quartier_resi_defunt', on_delete=models.CASCADE)

	DM_date = models.DateField(default=timezone.now, verbose_name='at_deces_dom_date_deces')

	date = models.DateField(default=timezone.now)

	first_witness = models.ForeignKey(Profile, related_name='at_deces_dom_T1',max_length=64, on_delete=models.CASCADE)
	second_witness = models.ForeignKey(Profile, related_name='at_deces_dom_T2',max_length=64, on_delete=models.CASCADE)
	
	rejection_msg = models.TextField(null=True, blank=True)
	secretary_validated = models.BooleanField(default=False, null=True, blank=True)
	ready = models.BooleanField(default=False)

	def price(self):
		try:
			return PriceHistory.objects.filter(zone=self.zone).last().total()
		except:
			return 0

	def requirements():
		return ["presence  physique et CNI du declarant","presence et CNI de deux temoins",]


	def save(self, *args, **kwargs):
		super(Document, self).save(*args, **kwargs)
		if self.ready:
			Notification(self.user, f"l'attestation de déces à domicile que vous avez demandé le {self.date} à {self.zone} est disponible").save()

	# def paymentPercent(self):
	# 	return 100 if self.zone_payment else 0

	# def validationPercent(self):
	# 	return 100 if self.secretary_validated  else 0

	def __str__(self):
		return f"{self.user} {self.zone}"

	# def onlyPaid(): # /!\ sans self
	# 	return Document.objects.filter(zone_payment__isnull = False)
	# 	# tout les filter necessaire en fait pas seulement zone
	# 	# si il y a pas de payments requises : return Document.objects.all()




# class PriceHistory(models.Model):
# 	date = models.DateField()
# 	zone = models.ForeignKey(Zone, related_name="deces9_domicile_price_province", on_delete=models.CASCADE)
# 	zone_price = models.IntegerField(default=0)
	
# 	def total(self):
# 		return self.zone_price