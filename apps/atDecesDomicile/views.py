import os
from apps.base.views import disconnect, Register
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import View

from apps.base.models import *
from .forms import DocumentForm
from .models import *

BASE_NAME = os.path.split(os.path.split(os.path.abspath(__file__))[0])[1]

PREFIX_DOC_TEMP = "decesdom"

class SecretaryListView(LoginRequiredMixin, View):
	template_name = PREFIX_DOC_TEMP+"_secr_list.html"
	def get(self, request, document_id=None, *args, **kwargs):
		documents = Document.objects.all()
		return render(request, self.template_name, locals())

class SecretaryView(LoginRequiredMixin, View):
	template_name = PREFIX_DOC_TEMP+"_secr_edit.html"

	def get(self, request, document_id, *args, **kwargs):
		deces_dom = get_object_or_404(Document, id=document_id)
		return render(request, self.template_name, locals())

	def post(self, request, document_id, *args, **kwargs):
		deces_dom = get_object_or_404(Document, id=document_id)
		if "reject" in request.POST:
			deces_dom.rejection_msg = request.POST["rejection_msg"]
			deces_dom.secretary_validated = True
			deces_dom.save()
			return redirect(BASE_NAME+'_secr_list')

		if "cancel" in request.POST:
			pass
		if "validate" in request.POST:
			deces_dom.secretary_validated = True
			deces_dom.save()
			return redirect(BASE_NAME+'_secr_list')
		return render(request, self.template_name, locals())



class DocumentListView(LoginRequiredMixin, View):
	template_name = PREFIX_DOC_TEMP+"_list.html"

	def get(self, request, document_id=None, *args, **kwargs):
		formurl = BASE_NAME+"_form"
		payform = BASE_NAME+"_pay_form"
		documents = Document.objects.filter(user=request.user)
		print(documents)
		return render(request, self.template_name, locals())


class DocumentFormView(LoginRequiredMixin, View):
	template_name = PREFIX_DOC_TEMP+"_form.html"
	quarters = Quarter.objects.all()
	zones = Zone.objects.all()
	profiles =Profile.objects.all()

	def get(self, request, *args, **kwargs):
		quarters = self.quarters 
		zones = self.zones 
		profiles = self.profiles
		form = DocumentForm()
		return render(request, self.template_name, locals())

	def post(self, request, *args, **kwargs):
		quarters = self.quarters 
		zones = self.zones
		profiles = self.profiles
		form = DocumentForm(request.POST)
		if "create" in request.POST:
			disconnect()
			return redirect("register")
		if "preview" in request.POST:
			preview = True
		if "cancel" in request.POST:
			preview = False
		if "submit" in request.POST:
			if form.is_valid():
				deces_dom = form.save(commit=False)
				deces_dom.user = request.user
				deces_dom.save()
				return redirect("home")
			return render(request, self.template_name, locals())
		if form.is_valid():
			deces_dom = form.save(commit=False)
			deces_dom.user = request.user
		return render(request, self.template_name, locals())


class MDocumentFormView(LoginRequiredMixin, View):
	template_name = PREFIX_DOC_TEMP+"_M_form.html"
	quarters = Quarter.objects.all()
	zones = Zone.objects.all()
	profiles =Profile.objects.all()

	def get(self, request, *args, **kwargs):
		quarters = self.quarters 
		zones = self.zones 
		profiles = self.profiles
		form = DocumentForm()
		return render(request, self.template_name, locals())

	def post(self, request, *args, **kwargs):
		quarters = self.quarters 
		zones = self.zones
		profiles = self.profiles
		form = DocumentForm(request.POST)
		if "preview" in request.POST:
			preview = True
		if "cancel" in request.POST:
			preview = False
		if "submit" in request.POST:
			if form.is_valid():
				deces_dom = form.save(commit=False)
				deces_dom.user = request.user
				deces_dom.save()
				return redirect("home")
			return render(request, self.template_name, locals())
		if form.is_valid():
			deces_dom = form.save(commit=False)
			deces_dom.user = request.user
		return render(request, self.template_name, locals())

class DocumentPayView(LoginRequiredMixin, View):
	template_name = PREFIX_DOC_TEMP+"_pay_form.html"

	def get(self, request, deces_dom, *args, **kwargs):
		payform = BASE_NAME+"_payform"
		document = Document.objects.get(id=deces_dom)
		if document.zone_payment:
			return redirect(BASE_NAME+"_list")
		form = PaymentZoneForm()
		return render(request, self.template_name, locals())

	def post(self, request, deces_dom, *args, **kwargs):
		payform = BASE_NAME+"_payform"
		document = Document.objects.get(id=deces_dom)
		form = PaymentZoneForm(request.POST, request.FILES)
		if form.is_valid():
			zone_payment = form.save(commit=False)
			zone_payment.place = document.zone
			zone_payment.save()
			document.zone_payment = zone_payment
			document.save()
			return redirect(BASE_NAME+"_list")
		return render(request, self.template_name, locals())

