import os

from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import View
from django.contrib import messages

from .forms import *
from apps.base.forms import *
from .models import *

BASE_NAME = os.path.split(os.path.split(os.path.abspath(__file__))[0])[1]
PREFIX_DOC_TEMP = "recom"

class SecretaryListView(LoginRequiredMixin, View):
	template_name = PREFIX_DOC_TEMP+"_secr_list.html"
	def get(self, request, document_id=None, *args, **kwargs):
		validation_form = ValidationForm()
		documents = Document.onlyPaid()
		return render(request, self.template_name, locals())

class SecretaryView(LoginRequiredMixin, View):
	template_name = PREFIX_DOC_TEMP+"_secr_edit.html"

	def get(self, request, document_id, *args, **kwargs):
		validation_form = ValidationForm()
		recomm = get_object_or_404(Document, id=document_id)
		return render(request, self.template_name, locals())

	def post(self, request, document_id, *args, **kwargs):
		validation_form = ValidationForm(request.POST)
		if(validation_form.is_valid()):
			print(request.POST)
			if "reject" in request.POST:
				notification = "Document mwasavye yanswe bivuye kuri ibi bikurikira : \n"
				notification +="\n Inomero :  "+ validation_form.cleaned_data["cni"] +" : ntizihuye"
				notification +="\n Code :  "+ validation_form.cleaned_data["payment"] +" : siyo"
				work_doc_copy
				return(notification)

			if "ready" in request.POST:
				pass
			if "valid" in request.POST:
				recomm.secretary_validated = True
				recomm.save()
				return redirect(BASE_NAME+'_secr_list')
		return render(request, self.template_name, locals())


class DocumentListView(LoginRequiredMixin, View):
	template_name = PREFIX_DOC_TEMP+'_list.html'

	def get(self, request, document_id=None, *args, **kwargs):
		formurl = BASE_NAME+'_form'
		payform = BASE_NAME+'_payform'
		documents = Document.objects.filter(user=request.user)
		print(documents)
		return render(request, self.template_name, locals())

	def delete_view(self, request, document_id, *args, **kwargs):
		delete = BASE_NAME+'_deleteDoc'
		document = Document.objects.get(id=document_id)
		return redirect(BASE_NAME+'_list')



class DocumentFormView(LoginRequiredMixin, View):
	template_name = PREFIX_DOC_TEMP+"_form.html"
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
		form = DocumentForm(request.POST, request.FILES)
		if "preview" in request.POST:
			if form.is_valid():
				preview = True
		if "cancel" in request.POST:
				preview = False
		if "submit" in request.POST:
			if form.is_valid():
				recomm = form.save(commit=False)
				recomm.user = request.user
				recomm.residence_quarter = request.user.profil.residence
				recomm.save()
				messages.success(request, "Document Soumis avec Succes ! ")
				return redirect(BASE_NAME+"_payform", recomm.id)
			return render(request, self.template_name, locals())
		if form.is_valid():
			recomm = form.save(commit=False)
			recomm.user = request.user
			recomm.residence_quarter = request.user.profil.residence
		return render(request, self.template_name, locals())

class DocumentPayView(LoginRequiredMixin, View):
	template_name = PREFIX_DOC_TEMP+"_pay_form.html"

	def get(self, request, document_id, *args, **kwargs):
		payform = BASE_NAME+"_payform"
		document = Document.objects.get(id=document_id)
		price = document.price()
		print("\n###############################\n")
		print(price)
		print("\n###############################\n")
		if document.zone_payment:
			return redirect(BASE_NAME+"_list")
		form = PaymentZoneForm()
		return render(request, self.template_name, locals())

	def post(self, request, document_id, *args, **kwargs):
		payform = BASE_NAME+"_payform"
		document = Document.objects.get(id=document_id)
		form = PaymentZoneForm(request.POST, request.FILES)
		if form.is_valid():
			zone_payment = form.save(commit=False)
			zone_payment.place = document.zone
			zone_payment.save()
			document.zone_payment = zone_payment
			document.save()
			return redirect(BASE_NAME+"_list")
		return render(request, self.template_name, locals())


# class DocumentDeleteView(LoginRequiredMixin, View):
# 	template_name = PREFIX_DOC_TEMP+'_del.html'

# 	def get(self, request, document_id, *args, **kwargs):
# 		delete = BASE_NAME+'_delconfirm'
# 		document = Document.objects.get(id=document_id)
# 		return render(request, self.template_name, locals())

# 	def post(self, request, document_id, *args, **kwargs):
# 		delete = BASE_NAME+'_delconfirm'
# 		document = Document.objects.get(id=document_id)

# 		if "oui" in request.POST:
# 			document.delete()
# 			messages.success(request, "Document Supprimé avec Succes ! ")
# 			return redirect(BASE_NAME+'_list')

# 		if "non" in request.POST:
# 			return redirect(BASE_NAME+'_list')

# 		return render(request, self.template_name, locals())


