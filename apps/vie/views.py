import os

from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import View

from .forms import DocumentForm
from apps.base.forms import *
from .models import *

BASE_NAME = os.path.split(os.path.split(os.path.abspath(__file__))[0])[1]

class SecretaryListView(LoginRequiredMixin, View):
	template_name = "vie_secr_list.html"
	def get(self, request, document_id=None, *args, **kwargs):
		documents = Document.onlyPaid()
		return render(request, self.template_name, locals())

class SecretaryView(LoginRequiredMixin, View):
	template_name = "vie_secr_edit.html"

	def get(self, request, document_id, *args, **kwargs):
		vie = get_object_or_404(Document, id=document_id)
		return render(request, self.template_name, locals())

	def post(self, request, document_id, *args, **kwargs):
		vie = get_object_or_404(Document, id=document_id)
		if "reject" in request.POST:
			vie.rejection_msg = request.POST["rejection_msg"]
			vie.secretary_validated = True
			vie.save()
			return redirect(BASE_NAME+'_secr_list')

		if "cancel" in request.POST:
			pass
		if "validate" in request.POST:
			vie.secretary_validated = True
			vie.save()
			return redirect(BASE_NAME+'_secr_list')
		return render(request, self.template_name, locals())

class DocumentListView(LoginRequiredMixin, View):
	template_name = "vie_list.html"
	def get(self, request, document_id=None, *args, **kwargs):
		formurl = BASE_NAME+"_form"
		payform = BASE_NAME+"_payform"
		documents = Document.objects.filter(user=request.user)
		print(documents)
		return render(request, self.template_name, locals())


class SecretaryPayView(LoginRequiredMixin, View):
	template_name = "vie_secr_pay.html"

	def get(self, request, document_id, *args, **kwargs):
		modal_mode = False
		vie = get_object_or_404(Document, id=document_id)
		return render(request, self.template_name, locals())

		
class DocumentFormView(LoginRequiredMixin, View):
	template_name = "vie_form.html"
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
		form = DocumentForm(request.POST)
		if "preview" in request.POST:
			preview = True
		if "cancel" in request.POST:
			preview = False
		if "submit" in request.POST:
			if form.is_valid():
				vie = form.save(commit=False)
				vie.user = request.user
				vie.save()
				return redirect("home")
			return render(request, self.template_name, locals())
		if form.is_valid():
			vie = form.save(commit=False)
			vie.user = request.user
		return render(request, self.template_name, locals())




class DocumentPayView(LoginRequiredMixin, View):
	template_name = "vie_pay_form.html"

	def get(self, request, vie, *args, **kwargs):
		payform = BASE_NAME+"_payform"
		document = Document.objects.get(id=vie)
		if document.zone_payment:
			return redirect(BASE_NAME+"_list")
		form = PaymentZoneForm()
		return render(request, self.template_name, locals())

	def post(self, request, vie, *args, **kwargs):
		payform = BASE_NAME+"_payform"
		document = Document.objects.get(id=vie)
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