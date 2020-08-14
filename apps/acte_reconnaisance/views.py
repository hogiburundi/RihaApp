import os

from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import View

from .forms import *
from apps.base.forms import *
from apps.base.models import *
from .models import *
from django.contrib import messages

BASE_NAME = os.path.split(os.path.split(os.path.abspath(__file__))[0])[1]

class SecretaryListView(LoginRequiredMixin, View):
	template_name = "acte_reco_secr_list.html"
	def get(self, request, document_id=None, *args, **kwargs):
		documents = Document.objects.all()
		isInProfile = get_object_or_404(Profile,user=request.user)
		isSecretary = ZonePersonnel.objects.filter(profile=isInProfile, user_level=2)
		if not isSecretary:
			return redirect("home")
		return render(request, self.template_name, locals())

class SecretaryView(LoginRequiredMixin, View):
	template_name = "acte_reco_secr_edit.html"

	def get(self, request, document_id, *args, **kwargs):
		acte_reconnais = get_object_or_404(Document, id=document_id)
		profiles = get_object_or_404(Profile, user=request.user)
		isSecretary = ZonePersonnel.objects.filter(profile=profiles, user_level=2)
		if not isSecretary:
			return redirect("home")
		return render(request, self.template_name, locals())

	def post(self, request, document_id, *args, **kwargs):
		acte_reconnais = get_object_or_404(Document, id=document_id)
		if "reject" in request.POST:
			acte_reconnais.rejection_msg = request.POST["rejection_msg"]
			acte_reconnais.secretary_validated = True
			acte_reconnais.save()
			messages.success(request, "Action is done!")
			return redirect(BASE_NAME+'_secr_list')

		if "cancel" in request.POST:
			pass
		if "validate" in request.POST:
			acte_reconnais.secretary_validated = True
			acte_reconnais.save()
			return redirect(BASE_NAME+'_secr_list')
		return render(request, self.template_name, locals())

class DocumentListView(LoginRequiredMixin, View):
	template_name = "acte_reco_list.html"
	def get(self, request, document_id=None, *args, **kwargs):
		formurl = BASE_NAME+"_form"
		payform = BASE_NAME+"_payform"
		documents = Document.objects.filter(user=request.user)
		print(documents)
		return render(request, self.template_name, locals())

class DocumentFormView(LoginRequiredMixin, View):
	template_name = "acte_reco_form.html"
	quarters = Quarter.objects.all()
	zones = Zone.objects.all()

	def get(self, request, *args, **kwargs):
		quarters = self.quarters 
		zones = self.zones 
		form = DocumentForm()
		return render(request, self.template_name, locals())

	def post(self, request, *args, **kwargs):
		quarters = self.quarters 
		zones = self.zones
		profiles = get_object_or_404(Profile, user=request.user ) 
		form = DocumentForm(request.POST)
		if "preview" in request.POST:
			if form.is_valid():
				preview = True
				cni_t11 = form.cleaned_data["cnis11"]
				cni_t12 = form.cleaned_data["cnis12"]
				cni_t21 = form.cleaned_data["cnis13"]
				cni_t22 = form.cleaned_data["cnis14"]

				check_cni_t11 = get_object_or_404(Profile, CNI=cni_t11)
				check_cni_t12 = get_object_or_404(Profile, CNI=cni_t12)
				check_cni_t13 = get_object_or_404(Profile, CNI=cni_t21)
				check_cni_t14 = get_object_or_404(Profile, CNI=cni_t22)
				
				
		if "cancel" in request.POST:
			preview = False
		if "submit" in request.POST:
			if form.is_valid():
				cni_t11 = form.cleaned_data["cnis11"]
				cni_t12 = form.cleaned_data["cnis12"]
				cni_t21 = form.cleaned_data["cnis13"]
				cni_t22 = form.cleaned_data["cnis14"]

				check_cni_t11 = get_object_or_404(Profile, CNI=cni_t11)
				check_cni_t12 = get_object_or_404(Profile, CNI=cni_t12)
				check_cni_t13 = get_object_or_404(Profile, CNI=cni_t21)
				check_cni_t14 = get_object_or_404(Profile, CNI=cni_t22)

				acte_reconnais = form.save(commit=False)
				acte_reconnais.user = request.user
				acte_reconnais.zone = profiles.quarter.zone
				acte_reconnais.residence_quarter = profiles.residence
				acte_reconnais.witness1 = str(check_cni_t11.user.last_name+" "+check_cni_t11.user.first_name)
				acte_reconnais.witness2 = str(check_cni_t12.user.last_name+" "+check_cni_t12.user.first_name)
				acte_reconnais.day_month_year = form.cleaned_data['day_month_year']
				acte_reconnais.work = profiles.job
				acte_reconnais.wife = str(check_cni_t14.user.last_name+" "+check_cni_t14.user.first_name)
				acte_reconnais.wife_age = 2020 - check_cni_t14.birthdate.year
				acte_reconnais.wife_work = check_cni_t14.job
				acte_reconnais.wife_province = check_cni_t14.residence.zone.commune.province
				acte_reconnais.witness_work1 = check_cni_t11.job
				acte_reconnais.witness_work2 = check_cni_t12.job
				acte_reconnais.witness_province1 = check_cni_t11.residence.zone.commune.province
				acte_reconnais.witness_province2 = check_cni_t12.residence.zone.commune.province
				acte_reconnais.witness_age1 = 2020 - check_cni_t11.birthdate.year
				acte_reconnais.witness_age2 = 2020 - check_cni_t12.birthdate.year
				acte_reconnais.child = str(check_cni_t13.user.last_name+" "+check_cni_t13.user.first_name)
				acte_reconnais.child_date = form.cleaned_data['child_date']
				acte_reconnais.child_age = 2020 - check_cni_t13.birthdate.year
				acte_reconnais.witness_nationality1 = check_cni_t11.nationnalite
				acte_reconnais.witness_nationality2 = check_cni_t12.nationnalite
				acte_reconnais.wife_nationality = check_cni_t14.nationnalite
				acte_reconnais.witness_gender1 = check_cni_t11.gender
				acte_reconnais.witness_gender2 = check_cni_t12.gender
				acte_reconnais.child_gender3 = check_cni_t13.gender
				acte_reconnais.wife_gender3 = check_cni_t14.gender
				
				acte_reconnais.save()
				return redirect("../payform/"+str(acte_reconnais.id))
			return render(request, self.template_name, locals())
		if form.is_valid():
			acte_reconnais = form.save(commit=False)
			acte_reconnais.user = request.user
		return render(request, self.template_name, locals())

class DocumentPayView(LoginRequiredMixin, View):
	template_name = "acte_reco_pay_form.html"

	def get(self, request, acte_reconnais, *args, **kwargs):
		payform = BASE_NAME+"_payform"
		document = Document.objects.get(id=acte_reconnais)
		if document.zone_payment:
			return redirect(BASE_NAME+"_list")
		form = PaymentZoneForm()
		return render(request, self.template_name, locals())

	def post(self, request, acte_reconnais, *args, **kwargs):
		payform = BASE_NAME+"_payform"
		document = Document.objects.get(id=acte_reconnais)
		form = PaymentZoneForm(request.POST, request.FILES)
		if form.is_valid():
			zone_payment = form.save(commit=False)
			zone_payment.place = document.zone
			zone_payment.save()
			document.zone_payment = zone_payment
			document.save()
			messages.success(request, "Payment is done!")
			return redirect(BASE_NAME+"_list")
		return render(request, self.template_name, locals())

class SecretaryPayView(LoginRequiredMixin, View):
	template_name = "acte_reconnais_secr_pay.html"

	def get(self, request, document_id, *args, **kwargs):
		modal_mode = False
		acte_reconnais = get_object_or_404(Document, id=document_id)
		return render(request, self.template_name, locals())

