from django.contrib import admin
from .models import *

admin.site.register(Profile)
admin.site.register(Commune)
admin.site.register(Quarter)
admin.site.register(Zone)
admin.site.register(Province)
admin.site.register(ProvinceLeader)
admin.site.register(CommuneLeader)
admin.site.register(QuarterLeader)
admin.site.register(ZoneLeader)
admin.site.register(ProvinceSecretary)
admin.site.register(CommuneSecretary)
admin.site.register(QuarterSecretary)
admin.site.register(ZoneSecretary)
admin.site.register(UsedSN)
admin.site.register(PaymentQuarter)
admin.site.register(PaymentCommune)
admin.site.register(PaymentProvince)
admin.site.register(PaymentZone)
