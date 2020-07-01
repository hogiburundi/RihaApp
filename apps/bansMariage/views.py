import os
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import View
from apps.base.models import *
from .forms import DocumentForm
from .models import *
from django.forms import modelformset_factory


BASE_NAME = os.path.split(os.path.split(os.path.abspath(__file__))[0])[1]

PREFIX_DOC_TEMP = "bmariage"



def Incognito(request):

	BrideFormSet = modelformset_factory(Incognito, fields=('incognito_last_name',
															'incognito_first_name',
															'incognito_father_name',
															'incognito_mother_name',
															'incognito_birthday_name',
															'incognito_birth_quarter',
															'incognito_birth_zone',
															'incognito_birth_province',
															'incognito_nationality',
															'incognito_marital_statute',
															'incognito_marital_CNI'))
	if request.method =='POST':
		bride_form = BrideFormSet(request.POST)
		bride_form.save()
	bride_form = BrideFormSet(request.POST)

	

	return render(request, PREFIX_DOC_TEMP+"_incognito.html", locals())




class SecretaryListView(LoginRequiredMixin, View):
	template_name = PREFIX_DOC_TEMP+"_secr_list.html"
	def get(self, request, document_id=None, *args, **kwargs):
		documents = Document.objects.all()
		return render(request, self.template_name, locals())

class SecretaryView(LoginRequiredMixin, View):
	template_name = PREFIX_DOC_TEMP+"_secr_edit.html"

	def get(self, request, document_id, *args, **kwargs):
		id_compl = get_object_or_404(Document, id=document_id)
		return render(request, self.template_name, locals())

	def post(self, request, document_id, *args, **kwargs):
		id_compl = get_object_or_404(Document, id=document_id)
		if "reject" in request.POST:
			id_compl.rejection_msg = request.POST["rejection_msg"]
			id_compl.secretary_validated = True
			id_compl.save()
			return redirect(BASE_NAME+'_secr_list')

		if "cancel" in request.POST:
			pass
		if "validate" in request.POST:
			id_compl.secretary_validated = True
			id_compl.save()
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
		if "incognito" in request.POST:
			redirect(BASE_NAME+'incognito')
		if "preview" in request.POST:
			preview = True
		if "cancel" in request.POST:
			preview = False
		if "submit" in request.POST:
			if form.is_valid():
				id_compl = form.save(commit=False)
				id_compl.user = request.user
				id_compl.save()
				return redirect("home")
			return render(request, self.template_name, locals())
		if form.is_valid():
			id_compl = form.save(commit=False)
			id_compl.user = request.user
		return render(request, self.template_name, locals())

class DocumentPayView(LoginRequiredMixin, View):
	template_name = PREFIX_DOC_TEMP+"_pay_form.html"

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
		return render(request, self.template_name, locals())

