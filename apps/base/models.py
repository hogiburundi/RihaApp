from django.db import models
from django.contrib.auth.models import User, Group
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
USER_LEVEL_DICT = dict([x[::-1] for x in [y for y in USER_LEVEL]])

PRIORITY_LEVEL = ( 
    (1, "Normal"), 
    (2, "Elevée"), 
)

try:
	SECRETARY_GROUP = Group.objects.get_or_create(name="secretary")[0]
	LEADER_GROUP = Group.objects.get_or_create(name="leader")[0]
except Exception as e:
	pass

def addInGroup(user, user_level):
	groups = user.groups.all()
	if user_level == 1:
		group = LEADER_GROUP
	elif user_level == 2:
		group = SECRETARY_GROUP
	else:
		group = -1
	if group!=-1 and group not in groups:
		user.groups.add(group)

def removeFromGroup(user, user_level):
	groups = user.groups.all()
	if user_level == 1:
		group = LEADER_GROUP
	elif user_level == 2:
		group = SECRETARY_GROUP
	else:
		group = -1
	if group!=-1 and group in groups:
		user.groups.remove(group)

class Profile(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE)
	gender = models.CharField(max_length=64, choices=GENDERS)
	nationnalite = models.CharField(max_length=64)
	quarter = models.ForeignKey('Quarter', related_name="user_quarter_residence", null=True, blank=True, on_delete=models.SET_NULL)
	address = models.CharField(max_length=64)
	CNI = models.CharField(max_length=64, null=True, blank=True)
<<<<<<< HEAD

	#==================================================== 	Aded 	==================================================================
	zone_delivery_CNI = models.ForeignKey('Zone', related_name='cni_released_zone', null=True, blank=True, on_delete=models.CASCADE)
	date_delivery_CNI = models.DateField()
	#=================================================================================================================================

	father = models.CharField(max_length=64, null=True, blank=True)
	mother = models.CharField(max_length=64, null=True, blank=True)
	birthdate = models.DateField()

	#========================================================= 	Aded 	=================================================================
	quarter_birth =  models.ForeignKey('Quarter', related_name="user_quarter_birth", null=True, blank=True, on_delete=models.SET_NULL)
	#====================================================================================================================================

=======
	# date_delivrated = models.DateTimeField()
	father = models.CharField(max_length=64, null=True, blank=True)
	mother = models.CharField(max_length=64, null=True, blank=True)
	birthdate = models.DateField(null=True)
>>>>>>> origin/master
	is_married = models.BooleanField(default=False, blank=True)
	cni_recto = models.ImageField(upload_to='cnis/', null=True, blank=True)
	cni_verso = models.ImageField(upload_to='cnis/', null=True, blank=True)
	job = models.CharField(max_length=64, null=True)
	prefix = models.CharField(max_length=12, null=True)
	# always required
	colline_natal           = models.CharField(max_length = 64)
	commune_natal     = models.CharField(max_length = 64)
	province_natal    = models.CharField(max_length = 64)
	

	def __str__(self):
		return f"{self.user.last_name} {self.user.first_name}"

class Notification(models.Model):
	user = models.ForeignKey(User, on_delete=models.CASCADE)
	message = models.CharField(max_length=128)
	seen = models.BooleanField(default=False)
	date = models.DateTimeField(default=timezone.now)

class PlaceModel(models.Model):
	name = models.CharField(max_length=64)
	ecocash = models.CharField(max_length=64, null=True)
	lumicash = models.CharField(max_length=64, null=True)
	bcb = models.CharField(max_length=64, null=True)
	# leader = models.ForeignKey("Profile", null=True, on_delete=models.SET_NULL, editable=False)

	class Meta:
		abstract = True

class Zone(PlaceModel):
	commune = models.ForeignKey('Commune', on_delete=models.CASCADE)
	
	def __str__(self):
		return f"{self.name} - {self.commune.province}"

class Province(PlaceModel):

	def __str__(self):
		return f"{self.name}"
	
class Commune(PlaceModel):
	province = models.ForeignKey('Province', on_delete=models.CASCADE)
	
	def __str__(self):
		return f"{self.name} - {self.province}"

class Quarter(PlaceModel):
	zone = models.ForeignKey('Zone', on_delete=models.CASCADE)

	def __str__(self):
		return f"{self.name} - {self.zone.name}"

class ModelPersonnel(models.Model):
	profile = models.ForeignKey("Profile", on_delete=models.CASCADE)
	user_level = models.IntegerField(choices=USER_LEVEL)
	sdate = models.DateTimeField(default=timezone.now)
	is_valid = models.BooleanField(default=True)
	edate = models.DateTimeField(null=True, blank=True)

	def __init__(self, *args, **kwargs):
		super(ModelPersonnel, self).__init__(*args, **kwargs)
		self.initial_user_level = self.user_level

	class Meta:
		abstract = True

	def save(self, *args, **kwargs):
		if self.initial_user_level != self.user_level:
			removeFromGroup(self.profile.user, self.initial_user_level)
			self.initial_user_level = self.user_level
		super(ModelPersonnel, self).save(*args, **kwargs)
		self.checkGroup()

	def checkGroup(self):
		if self.is_valid:
			addInGroup(self.profile.user, self.user_level)
		else:
			removeFromGroup(self.profile.user, self.user_level)
			if not self.edate:
				self.edate = timezone.now()
				self.save()

class ZonePersonnel(ModelPersonnel):
	zone = models.ForeignKey("Zone", null=True, on_delete=models.SET_NULL)
	
	def __str__(self):
		return f"{self.profile} - {self.zone}"

class ProvincePersonnel(ModelPersonnel):
	province = models.ForeignKey("Province", null=True, on_delete=models.SET_NULL)
	
	def __str__(self):
		return f"{self.profile} - {self.province}"
	
class CommunePersonnel(ModelPersonnel):
	commune = models.ForeignKey("Commune", null=True, on_delete=models.SET_NULL)
	
	def __str__(self):
		return f"{self.profile} - {self.commune}"

class QuarterPersonnel(ModelPersonnel):
	quarter = models.ForeignKey("Quarter", null=True, on_delete=models.SET_NULL)
	
	def __str__(self):
		return f"{self.profile} - {self.quarter}"

class ModelPayement(models.Model):
	type_payement = models.CharField(choices=PAYMENTS, max_length=64)
	id_transaction = models.CharField(max_length=64)
	bordereau = models.ImageField(upload_to='bordereaux/', null=True, blank=True)
	date = models.DateTimeField(default=timezone.now)
	is_valid = models.BooleanField(default=False)
	
	class Meta:
		abstract = True

	def save(self, *args, **kwargs):
		super(ModelPayement, self).save(*args, **kwargs)
		UsedSN(self.id_transaction, self.type_payement).save()

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
	
	def __str__(self):
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