from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.db.models.signals import post_save, pre_save

GENDERS = (
	("H", 'Homme'),
	("F", "Femme")
)

PAYMENTS = ( 
    ("ecocash", "Ecocash"), 
    ("lumicash", "Lumicash"), 
    ("bcb", "BCB"), 
)

PLACE_LEVEL = ( 
    (1, "Pays"), 
    (2, "Province"), 
    (3, "Commune"), 
    (4, "Quarter"), 
    (5, "Zone")
)
PLACE_LEVEL_DICT = dict([x[::-1] for x in [y for y in PLACE_LEVEL]])

USER_LEVEL = ( 
    (1, "Chef"), 
    (2, "Secretaire"), 
) 

PRIORITY_LEVEL = ( 
    (1, "Normal"), 
    (2, "Elevée"), 
) 

class Profile(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE)
	gender = models.CharField(max_length=64, choices=GENDERS)
	nationnalite = models.CharField(max_length=64)
	quarter = models.ForeignKey('Quarter', null=True, blank=True, on_delete=models.SET_NULL)
	address = models.CharField(max_length=64)
	CNI = models.CharField(max_length=64, null=True, blank=True)
	# father = models.ForeignKey(User, related_name='father', null=True, blank=True, on_delete=models.SET_NULL)
	# mother = models.ForeignKey(User, related_name='mother', null=True, blank=True, on_delete=models.SET_NULL)
	father = models.CharField(max_length=64, null=True, blank=True)
	mother = models.CharField(max_length=64, null=True, blank=True)
	birthdate = models.DateField()
	is_married = models.BooleanField(default=False, blank=True)
	cni_recto = models.ImageField(upload_to='cnis/', null=True, blank=True)
	cni_verso = models.ImageField(upload_to='cnis/', null=True, blank=True)
	job = models.CharField(max_length=64)

	def __str__(self):
		return f"{self.user.last_name} {self.user.first_name}"

class Notification(models.Model):
	user = models.ForeignKey(User, on_delete=models.CASCADE)
	message = models.CharField(max_length=128)
	seen = models.BooleanField(default=False)
	date = models.DateTimeField(default=timezone.now)

class Zone(models.Model):
	name = models.CharField(max_length=64)
	commune = models.ForeignKey('Commune', on_delete=models.CASCADE)
	ecocash = models.CharField(max_length=64, null=True, blank=True)
	lumicash = models.CharField(max_length=64, null=True, blank=True)
	bcb = models.CharField(max_length=64, null=True, blank=True)

	def __str__(self):
		return f"{self.name} - {self.commune.province}"

class Province(models.Model):
	name = models.CharField(max_length=64)
	ecocash = models.CharField(max_length=64, null=True)
	lumicash = models.CharField(max_length=64, null=True)
	bcb = models.CharField(max_length=64, null=True)

	def __str__(self):
		return f"{self.name}"
	
class Commune(models.Model):
	name = models.CharField(max_length=64)
	province = models.ForeignKey('Province', on_delete=models.CASCADE)
	ecocash = models.CharField(max_length=64, null=True, blank=True)
	lumicash = models.CharField(max_length=64, null=True, blank=True)
	bcb = models.CharField(max_length=64, null=True, blank=True)

	def __str__(self):
		return f"{self.name} - {self.province}"

class Quarter(models.Model):
	name = models.CharField(max_length=64)
	zone = models.ForeignKey('Zone', on_delete=models.CASCADE)
	ecocash = models.CharField(max_length=64, null=True, blank=True)
	lumicash = models.CharField(max_length=64, null=True, blank=True)
	bcb = models.CharField(max_length=64, null=True, blank=True)

	def __str__(self):
		return f"{self.name} - {self.zone.name}"

class ZoneLeader(models.Model):
	zone = models.ForeignKey("Zone", null=True, on_delete=models.SET_NULL)
	profile = models.ForeignKey("Profile", on_delete=models.CASCADE)

	def __str__(self):
		return f"{self.name} - {self.commune.province}"

class ProvinceLeader(models.Model):
	province = models.ForeignKey("Province", null=True, on_delete=models.SET_NULL)
	profile = models.ForeignKey("Profile", on_delete=models.CASCADE)
	def __str__(self):
		return f"{self.name}"
	
class CommuneLeader(models.Model):
	commune = models.ForeignKey("Commune", null=True, on_delete=models.SET_NULL)
	profile = models.ForeignKey("Profile", on_delete=models.CASCADE)

	def __str__(self):
		return f"{self.name} - {self.province}"

class QuarterLeader(models.Model):
	quarter = models.ForeignKey("Quarter", null=True, on_delete=models.SET_NULL)
	profile = models.ForeignKey("Profile", on_delete=models.CASCADE)

	def __str__(self):
		return f"{self.name} - {self.zone.name}"

class ZoneSecretary(models.Model):
	zone = models.ForeignKey("Zone", null=True, on_delete=models.SET_NULL)
	profile = models.ForeignKey("Profile", on_delete=models.CASCADE)

	def __str__(self):
		return f"{self.name} - {self.commune.province}"

class ProvinceSecretary(models.Model):
	province = models.ForeignKey("Province", null=True, on_delete=models.SET_NULL)
	profile = models.ForeignKey("Profile", on_delete=models.CASCADE)

	def __str__(self):
		return f"{self.name}"
	
class CommuneSecretary(models.Model):
	commune = models.ForeignKey("Commune", null=True, on_delete=models.SET_NULL)
	profile = models.ForeignKey("Profile", on_delete=models.CASCADE)

	def __str__(self):
		return f"{self.name} - {self.province}"

class QuarterSecretary(models.Model):
	quarter = models.ForeignKey("Quarter", null=True, on_delete=models.SET_NULL)
	profile = models.ForeignKey("Profile", on_delete=models.CASCADE)

	def __str__(self):
		return f"{self.name} - {self.zone.name}"

class ModelPayement(models.Model):
	type_payement = models.CharField(choices=PAYMENTS, max_length=64)
	id_transaction = models.CharField(max_length=64)
	bordereau = models.ImageField(upload_to='bordereaux/', null=True, blank=True)
	date = models.DateTimeField(default=timezone.now)
	is_valid = models.BooleanField(default=False)
	
	class Meta:
		abstract = True

class UsedSN(models.Model):
	id_transaction = models.CharField(max_length=64)
	name_transaction = models.CharField(max_length=64)

class ModelDocument(models.Model):
	document = models.CharField(max_length=64)
	is_valid = models.BooleanField(null=True)
	place_level = models.IntegerField(choices=PLACE_LEVEL)
	user_level = models.IntegerField(choices=USER_LEVEL)
	place_name = models.CharField(max_length=64)
	document_id = models.IntegerField()
	priority = models.IntegerField(choices=PRIORITY_LEVEL)

class PaymentQuarter(ModelPayement):
	place = models.ForeignKey('Quarter', related_name="quarter", on_delete=models.CASCADE)
	is_valid = models.BooleanField(null=True)

	def __str__():
		return f"{self.place} - {self.date} : {self.id_transaction}"

	class Meta:
		verbose_name_plural = "Payments per Quarter"

	def place_level(self):
		return PLACE_LEVEL_DICT["Quarter"]

class PaymentCommune(ModelPayement):
	place = models.ForeignKey('Commune', related_name="commune", on_delete=models.CASCADE)
	is_valid = models.BooleanField(null=True)
	
	def __str__():
		return f"{self.place} - {self.date} : {self.id_transaction}"

	class Meta:
		verbose_name_plural = "Payments per Commune"

	def place_level(self):
		return PLACE_LEVEL_DICT["Commune"]

class PaymentProvince(ModelPayement):
	place = models.ForeignKey('Province', related_name="province", on_delete=models.CASCADE)
	is_valid = models.BooleanField(null=True)
	
	def __str__():
		return f"{self.place} - {self.date} : {self.id_transaction}"

	class Meta:
		verbose_name_plural = "Payments per Province"

	def place_level(self):
		return PLACE_LEVEL_DICT["Province"]

class PaymentZone(ModelPayement):
	place = models.ForeignKey('Zone', related_name="zone", on_delete=models.CASCADE)
	is_valid = models.BooleanField(null=True)
	
	def __str__():
		return f"{self.place} - {self.date} : {self.id_transaction}"

	class Meta:
		verbose_name_plural = "Payments per Zone"

	def place_level(self):
		return PLACE_LEVEL_DICT["Zone"]

def createPaymentModelDocument(sender, instance, *args, **kwargs):
	self = instance
	ModelDocument(
		document = "payment",
		is_valid = self.is_valid,
		place_level = self.place_level,
		user_level = 2, # LEVEL Secretaire
		place_name = str(self.place),
		document_id = self.id,
		priority = 2 # Elevée
	)

def createUsedSN(sender, instance, *args, **kwargs):
	self = instance
	if self.is_valid:
		last_sn = UsedSN.objects.filter(id_transaction = self.id_transaction)

post_save.connect(createPaymentModelDocument, sender=ModelPayement)