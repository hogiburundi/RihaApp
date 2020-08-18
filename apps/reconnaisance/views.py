import os

from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import View

from .forms import *
from apps.base.forms import *
from .models import *
from apps.base.models import *
from django.contrib import messages

BASE_NAME = os.path.split(os.path.split(os.path.abspath(__file__))[0])[1]

class SecretaryListView(LoginRequiredMixin, View):
	template_name = "reconnaisance_secr_list.html"
	def get(self, request, document_id=None, *args, **kwargs):
		validation_form = ValidationForm()
		documents = Document.objects.all()
		isInProfile = get_object_or_404(Profile,user=request.user)
		isSecretary = ZonePersonnel.objects.filter(profile=isInProfile, user_level=2)
		if not isSecretary:
			return redirect("home")
		return render(request, self.template_name, locals())

class SecretaryView(LoginRequiredMixin, View):
	template_name = "reconnaisance_secr_edit.html"

	def get(self, request, document_id, *args, **kwargs):
		validation_form = ValidationForm()
		reconnais = get_object_or_404(Document, id=document_id)
		profiles = get_object_or_404(Profile, user=request.user)
		isSecretary = ZonePersonnel.objects.filter(profile=profiles, user_level=2)
		if not isSecretary:
			return redirect("home")
		return render(request, self.template_name, locals())

	def post(self, request, document_id, *args, **kwargs):
		validation_form = ValidationForm(request.POST)
		print(request)
		if(validation_form.is_valid()):
			document = get_object_or_404(Document, id=document_id)
			if "reject" in request.POST:
				document.secretary_validated=False
				notification = "attestation de reconnaissance yanyu yanswe. imvo: "
				notification+="\n- ifoto ya karangamuntu " if validation_form.cleaned_data["cni_recto"] or validation_form.cleaned_data["cni_verso"] else ""
				notification+="\n- ibibaranga bihushanye na karangamuntu " if validation_form.cleaned_data["cni"] else ""
				notification+="\n- amakuru yo kuriha " if validation_form.cleaned_data["payment"] else ""
				document.rejection_msg=notification
				document.save()
				Notification(user=document.user, message=notification).save()

			if "ready" in request.POST:
				document.ready=True
				notification = "attestation de reconnaissance yanyu yatunganye. murashobora kuza kuyitora mwibangikanije "
				notification += " ".join([x for x in Document.requirements()])
				Notification(user=document.user, message=notification).save()
				return redirect(BASE_NAME+"_secr_list")

			if "valid" in request.POST:
				document.secretary_validated = True
				document.save()
				return redirect(BASE_NAME+'_secr_list')
		return render(request, self.template_name, locals())

class DocumentListView(LoginRequiredMixin, View):
	template_name = "reconnaisance_list.html"
	def get(self, request, document_id=None, *args, **kwargs):
		formurl = BASE_NAME+"_form"
		payform = BASE_NAME+"_payform"
		documents = Document.objects.filter(user=request.user)
		print(documents)
		return render(request, self.template_name, locals())

class DocumentFormView(LoginRequiredMixin, View):
	template_name = "reconnaisance_form.html"
	quarters = Quarter.objects.all()
	zones = Zone.objects.all()

	def get(self, request, *args, **kwargs):
		form = DocumentForm()
		return render(request, self.template_name, locals())

	def post(self, request, *args, **kwargs):
		quarters = self.quarters 
		zones = self.zones 
		form = DocumentForm(request.POST)
		if "preview" in request.POST:
			if form.is_valid():
				preview = True
		if "cancel" in request.POST:
			preview = False
		if "submit" in request.POST:
			if form.is_valid():
				reconnais = form.save(commit=False)
				reconnais.user = request.user
				reconnais.save()
				return redirect("../payform/"+str(reconnais.id))
			return render(request, self.template_name, locals())
		if form.is_valid():
			reconnais = form.save(commit=False)
			reconnais.user = request.user
		return render(request, self.template_name, locals())


class DocumentPayView(LoginRequiredMixin, View):
	template_name = "reconnaisance_pay_form.html"

	def get(self, request, reconnais, *args, **kwargs):
		payform = BASE_NAME+"_payform"
		document = Document.objects.get(id=reconnais)
		if document.zone_payment:
			return redirect(BASE_NAME+"_list")
		form = PaymentZoneForm()
		return render(request, self.template_name, locals())

	def post(self, request, reconnais, *args, **kwargs):
		payform = BASE_NAME+"_payform"
		document = Document.objects.get(id=reconnais)
		form = PaymentZoneForm(request.POST, request.FILES)
		if form.is_valid():
			zone_payment = form.save(commit=False)
			zone_payment.place = document.association_quarter.zone
			zone_payment.save()
			document.zone_payment = zone_payment
			document.save()
			messages.success(request, "Payment is done!")
			return redirect(BASE_NAME+"_list")
		return render(request, self.template_name, locals())

class SecretaryPayView(LoginRequiredMixin, View):
	template_name = "reconnais_secr_pay.html"

	def get(self, request, document_id, *args, **kwargs):
		modal_mode = False
		reconnais = get_object_or_404(Document, id=document_id)
		return render(request, self.template_name, locals())

