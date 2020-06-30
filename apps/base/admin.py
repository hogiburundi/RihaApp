from django.contrib import admin
from .models import *

admin.site.register(Profile)
admin.site.register(Commune)
admin.site.register(Quarter)
admin.site.register(Zone)
admin.site.register(Province)
admin.site.register(ProvincePersonnel)
admin.site.register(CommunePersonnel)
admin.site.register(QuarterPersonnel)
admin.site.register(ZonePersonnel)
admin.site.register(UsedSN)
admin.site.register(PaymentQuarter)
admin.site.register(PaymentCommune)
admin.site.register(PaymentProvince)
admin.site.register(PaymentZone)
admin.site.site_header = "RIHA App"
