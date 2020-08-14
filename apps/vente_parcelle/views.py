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
	template_name = "vente_parcelle_secr_list.html"
	def get(self, request, document_id=None, *args, **kwargs):
		documents = Document.objects.all()
		isInProfile = get_object_or_404(Profile,user=request.user)
		isSecretary = ZonePersonnel.objects.filter(profile=isInProfile, user_level=2)
		if not isSecretary:
			return redirect("home")
		return render(request, self.template_name, locals())

class SecretaryView(LoginRequiredMixin, View):
	template_name = "vente_parcelle_secr_edit.html"

	def get(self, request, document_id, *args, **kwargs):
		vente_parcelle = get_object_or_404(Document, id=document_id)
		profiles = get_object_or_404(Profile, user=request.user)
		isSecretary = ZonePersonnel.objects.filter(profile=profiles, user_level=2)
		if not isSecretary:
			return redirect("home")
		return render(request, self.template_name, locals())

	def post(self, request, document_id, *args, **kwargs):
		vente_parcelle = get_object_or_404(Document, id=document_id)
		if "reject" in request.POST:
			vente_parcelle.rejection_msg = request.POST["rejection_msg"]
			vente_parcelle.secretary_validated = True
			vente_parcelle.save()
			messages.success(request, "Action is done!")
			return redirect(BASE_NAME+'_secr_list')

		if "cancel" in request.POST:
			pass
		if "validate" in request.POST:
			vente_parcelle.secretary_validated = True
			vente_parcelle.save()
			return redirect(BASE_NAME+'_secr_list')
		return render(request, self.template_name, locals())

class DocumentListView(LoginRequiredMixin, View):
	template_name = "vente_parcelle_list.html"
	def get(self, request, document_id=None, *args, **kwargs):
		formurl = BASE_NAME+"_form"
		payform = BASE_NAME+"_payform"
		documents = Document.objects.filter(user=request.user)
		print(documents)
		return render(request, self.template_name, locals())

class DocumentFormView(LoginRequiredMixin, View):
	template_name = "vente_parcelle_form.html"
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
				cni = form.cleaned_data["buyer"]
				cni_t11 = form.cleaned_data["cnis11"]
				cni_t12 = form.cleaned_data["cnis12"]
				cni_t21 = form.cleaned_data["cnis21"]
				cni_t22 = form.cleaned_data["cnis22"]

				check_cni = get_object_or_404(Profile, CNI=cni)
				check_cni_t11 = get_object_or_404(Profile, CNI=cni_t11)
				check_cni_t12 = get_object_or_404(Profile, CNI=cni_t12)
				check_cni_t21 = get_object_or_404(Profile, CNI=cni_t21)
				check_cni_t22 = get_object_or_404(Profile, CNI=cni_t22)

				if not check_cni:
					messages.error(request, "User doesn't exist")
				else:
					vente_parcelle = form.save(commit=False)
					vente_parcelle.user = request.user
					vente_parcelle.buyer = str(check_cni.user.first_name + " " + check_cni.user.last_name)


		if "cancel" in request.POST:
			preview = False

		if "submit" in request.POST:
			if form.is_valid():
				cni = form.cleaned_data["buyer"]
				cni_t11 = form.cleaned_data["cnis11"]
				cni_t12 = form.cleaned_data["cnis12"]
				cni_t21 = form.cleaned_data["cnis21"]
				cni_t22 = form.cleaned_data["cnis22"]

				check_cni = get_object_or_404(Profile, CNI=cni)
				check_cni_t11 = get_object_or_404(Profile, CNI=cni_t11)
				check_cni_t12 = get_object_or_404(Profile, CNI=cni_t12)
				check_cni_t21 = get_object_or_404(Profile, CNI=cni_t21)
				check_cni_t22 = get_object_or_404(Profile, CNI=cni_t22)

				vente_parcelle = form.save(commit=False)
				vente_parcelle.user = request.user
				vente_parcelle.zone = profiles.quarter.zone
				vente_parcelle.residence_quarter = profiles.residence
				vente_parcelle.buyer_name = str(check_cni.user.first_name+" "+check_cni.user.lasst_name)
				vente_parcelle.buyer_father = check_cni.father
				vente_parcelle.buyer_mother = check_cni.mother
				vente_parcelle.buyer_zone = check_cni.quarter.zone
				vente_parcelle.buyer_residence_quarter = check_cni.residence
				vente_parcelle.witness11 = str(check_cni_t11.user.first_name+" "+check_cni_t11.user.last_name)
				vente_parcelle.witness12 = str(check_cni_t12.user.first_name+" "+check_cni_t12.user.last_name)
				vente_parcelle.witness21 = str(check_cni_t21.user.first_name+" "+check_cni_t21.user.last_name)
				vente_parcelle.witness22 = str(check_cni_t22.user.first_name+" "+check_cni_t22.user.last_name)
				vente_parcelle.saler_witness_residence1 = check_cni_t11.residence
				vente_parcelle.saler_witness_residence2 = check_cni_t12.residence
				vente_parcelle.buyer_witness_residence1 = check_cni_t21.residence
				vente_parcelle.buyer_witness_residence2 = check_cni_t22.residence

				vente_parcelle.save()
				return redirect("../payform/"+str(vente_parcelle.id))
				
			return render(request, self.template_name, locals())
		if form.is_valid():
			vente_parcelle = form.save(commit=False)
			vente_parcelle.user = request.user
			vente_parcelle.zone = profiles.quarter.zone
			vente_parcelle.residence_quarter = profiles.residence
			vente_parcelle.buyer = str(check_cni.user.first_name + " " + check_cni.user.last_name)
			vente_parcelle.buyer_father = check_cni.father
			vente_parcelle.buyer_mother = check_cni.mother
			vente_parcelle.buyer_zone = check_cni.quarter.zone
			vente_parcelle.buyer_residence_quarter = check_cni.residence
			vente_parcelle.witness11 = str(check_cni_t11.user.first_name+" "+check_cni_t11.user.last_name)
			vente_parcelle.witness12 = str(check_cni_t12.user.first_name+" "+check_cni_t12.user.last_name)
			vente_parcelle.witness21 = str(check_cni_t21.user.first_name+" "+check_cni_t21.user.last_name)
			vente_parcelle.witness22 = str(check_cni_t22.user.first_name+" "+check_cni_t22.user.last_name)
			vente_parcelle.saler_witness_residence1 = check_cni_t11.residence
			vente_parcelle.saler_witness_residence2 = check_cni_t12.residence
			vente_parcelle.buyer_witness_residence1 = check_cni_t21.residence
			vente_parcelle.buyer_witness_residence2 = check_cni_t22.residence
		return render(request, self.template_name, locals())

	# def post(self, request, *args, **kwargs):
	# 	quarters = self.quarters 
	# 	zones = self.zones
	# 	profiles = get_object_or_404(Profile, user=request.user )
	# 	form = DocumentForm(request.POST)
	# 	if "preview" in request.POST:
	# 		if form.is_valid():
	# 			preview = True
	# 	if "cancel" in request.POST:
	# 		preview = False
	# 	if "submit" in request.POST:
	# 		if form.is_valid():
	# 			vente_parcelle = form.save(commit=False)
	# 			vente_parcelle.user = request.user
	# 			vente_parcelle.
	# 			vente_parcelle.save()
	# 			# return redirect("../payform/" + str(vente_parcelle.id))
	# 			messages.success(request, vente_parcelle.buyer)
	# 			# messages.success(request, "Continue with payment!")
	# 		return render(request, self.template_name, locals())
	# 	if form.is_valid():
	# 		vente_parcelle = form.save(commit=False)
	# 		vente_parcelle.user = request.user
	# 	return render(request, self.template_name, locals())


class DocumentPayView(LoginRequiredMixin, View):
	template_name = "vente_parcelle_pay_form.html"

	def get(self, request, vente_parcelle, *args, **kwargs):
		payform = BASE_NAME+"_payform"
		document = Document.objects.get(id=vente_parcelle)
		if document.zone_payment:
			return redirect(BASE_NAME+"_list")
		form = PaymentZoneForm()
		return render(request, self.template_name, locals())

	def post(self, request, vente_parcelle, *args, **kwargs):
		payform = BASE_NAME+"_payform"
		document = Document.objects.get(id=vente_parcelle)
		form = PaymentZoneForm(request.POST, request.FILES)
		if form.is_valid():
			zone_payment = form.save(commit=False)
			zone_payment.place = document.zone
			zone_payment.save()
			document.zone_payment = zone_payment
			document.save()
			messages.error(request, "Payment is done!")
			return redirect(BASE_NAME+"_list")
		return render(request, self.template_name, locals())

class SecretaryPayView(LoginRequiredMixin, View):
	template_name = "vente_parcelle_secr_pay.html"

	def get(self, request, document_id, *args, **kwargs):
		modal_mode = False
		vente_parcelle = get_object_or_404(Document, id=document_id)
		return render(request, self.template_name, locals())

