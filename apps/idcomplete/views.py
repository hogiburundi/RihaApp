import os

from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import View

from .forms import DocumentForm, ValidationForm
from apps.base.forms import *
from apps.base.models import *
from .models import *

BASE_NAME = os.path.split(os.path.split(os.path.abspath(__file__))[0])[1]

class SecretaryListView(LoginRequiredMixin, View):
	template_name = "idcomp_secr_list.html"
	def get(self, request, *args, **kwargs):
		validation_form = ValidationForm()
		documents = Document.onlyPaid()
		return render(request, self.template_name, locals())

class SecretaryView(LoginRequiredMixin, View):
	template_name = "idcomp_secr_edit.html"

	def get(self, request, document_id, *args, **kwargs):
		validation_form = ValidationForm()
		id_compl = get_object_or_404(Document, id=document_id)
		return render(request, self.template_name, locals())

	def post(self, request, document_id, *args, **kwargs):
		validation_form = ValidationForm(request.POST)
		print(request)
		if(validation_form.is_valid()):
			document = get_object_or_404(Document, id=document_id)
			if "reject" in request.POST:
				document.secretary_validated=False
				notification = "identite complete yanyu yanswe. imvo: "
				notification+="\n- ifoto ya karangamuntu " if validation_form.cleaned_data["cni_recto"] or validation_form.cleaned_data["cni_verso"] else ""
				notification+="\n- ibibaranga bihushanye na karangamuntu " if validation_form.cleaned_data["cni"] else ""
				notification+="\n- amakuru yo kuriha " if validation_form.cleaned_data["payment"] else ""
				document.rejection_msg=notification
				document.save()
				Notification(user=document.user, message=notification).save()

			if "ready" in request.POST:
				document.ready=True
				notification = "identite complete yanyu yatunganye. murashobora kuza kuyitora mwibangikanije "
				notification += " ".join([x for x in document.requirements()])
				Notification(user=document.user, message=notification).save()

			if "valid" in request.POST:
				document.secretary_validated = True
				document.save()
				return redirect(BASE_NAME+'_secr_list')
		return render(request, self.template_name, locals())

class SecretaryPayView(LoginRequiredMixin, View):
	template_name = "idcomp_secr_pay.html"

	def get(self, request, document_id, *args, **kwargs):
		modal_mode = False
		id_compl = get_object_or_404(Document, id=document_id)
		return render(request, self.template_name, locals())

class DocumentListView(LoginRequiredMixin, View):
	template_name = "idcomp_list.html"
	def get(self, request, document_id=None, *args, **kwargs):
		formurl = BASE_NAME+"_form"
		payform = BASE_NAME+"_payform"
		documents = Document.objects.filter(user=request.user)
		print(documents)
		return render(request, self.template_name, locals())

class DocumentFormView(LoginRequiredMixin, View):
	template_name = "idcomp_form.html"

	def get(self, request, *args, **kwargs):
		form = DocumentForm(initial = {'residence_quarter': request.user.profile.residence })
		return render(request, self.template_name, locals())

	def post(self, request, *args, **kwargs):
		form = DocumentForm(request.POST)
		if "preview" in request.POST:
			preview = True
		if "cancel" in request.POST:
			preview = False
		if "submit" in request.POST:
			if form.is_valid():
				id_compl = form.save(commit=False)
				id_compl.user = request.user
				id_compl.save()
				return redirect(BASE_NAME+"_payform", id_compl=id_compl.id)
			return render(request, self.template_name, locals())
		if form.is_valid():
			id_compl = form.save(commit=False)
			id_compl.user = request.user
		return render(request, self.template_name, locals())


class DocumentPayView(LoginRequiredMixin, View):
	template_name = "idcomp_pay_form.html"

	def get(self, request, id_compl, *args, **kwargs):
		payform = BASE_NAME+"_payform"
		document = Document.objects.get(id=id_compl)
		if document.zone_payment:
			return redirect(BASE_NAME+"_list")
		form = PaymentZoneForm()
		return render(request, self.template_name, locals())

	def post(self, request, id_compl, *args, **kwargs):
		payform = BASE_NAME+"_payform"
		document = Document.objects.get(id=id_compl)
		form = PaymentZoneForm(request.POST, request.FILES)
		if form.is_valid():
			zone_payment = form.save(commit=False)
			zone_payment.place = document.zone
			zone_payment.save()
			document.zone_payment = zone_payment
			document.save()
			return redirect(BASE_NAME+"_list")
		print(form)
		return render(request, self.template_name, locals())

