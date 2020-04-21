from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from apps.base.models import *

class IdComplete(models.Model):
	user = models.ForeignKey(User, on_delete=models.CASCADE)
	zone = models.ForeignKey(Zone, max_length=64, on_delete=models.CASCADE)
	residence_quarter = models.ForeignKey(Quarter, max_length=64, on_delete=models.CASCADE)
	CNI = models.CharField(max_length=64)
	date = models.DateField(default=timezone.now)
	payment_method = models.CharField(max_length=64)
	payment_serial = models.CharField(max_length=64)
	secretary_validated = models.BooleanField(default=False)
	ready = models.BooleanField(default=False)

	def price():
		return {"mairie":500}

	def requirements():
		return ["cahier de menage", ]