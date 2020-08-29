import os

from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import View
from django.contrib import messages
from django.contrib.auth.decorators import login_required

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
				document.secretary_validated=False
				notification = "Attestation de naissance à domicile yanyu yanswe. imvo: \n"
				notification += "\n- Ifoto yawe ya karangamuntu " if validation_form.cleaned_data["cni_recto_declarant"] or validation_form.cleaned_data["cni_verso_declarant"] else "" 
				notification += "\n- Inomero ya karangamuntu yawe siyo " if validation_form.cleaned_data["cni_declarant"] else "" 
				notification +="\n- Amakuru yo kuriha siyo :  " if validation_form.cleaned_data["payment"] else ""
				work_doc_copy += "\n- Urupapuro rwerekana akazi mukora rurahajije " if validation_form.cleaned_data["work_doc_copy"] else ""
				document.rejection_msg = notification
				document.save()
				Notification(user=document.user, messages=document.notification)
				return(notification)

			if "ready" in request.POST:
				document.ready = True
				notification = "Attestationde recommendation mwasavye yatunganijwe.\n Muze mwibangikanije : "
				notification += " ".join([x for x in Document.requirements()])
				Notification(user=document.user, message=notification).save()
				return redirect(BASE_NAME+"_secr_list")
				
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
		delete = BASE_NAME+'_delete'
		update = BASE_NAME+'_update'
		clone = BASE_NAME+'_clone'
		documents = Document.objects.filter(user=request.user)
		print(documents)
		return render(request, self.template_name, locals())


class DocumentFormView(LoginRequiredMixin, View):
	template_name = PREFIX_DOC_TEMP+"_form.html"
	quarters = Quarter.objects.all()
	zones = Zone.objects.all()

	def get(self, request, *args, **kwargs):
		quarters = self.quarters 
		zones = self.zones 
		form = DocumentForm(request.FILES, initial={'zone':request.user.profile.residence.zone.name})
		return render(request, self.template_name, locals())

	def post(self, request, *args, **kwargs):
		quarters = self.quarters 
		zones = self.zones 
		form = DocumentForm(request.POST, request.FILES,initial={'zone':request.user.profile.residence.zone.name})
		if "preview" in request.POST:
			if form.is_valid():
				preview = True
		if "cancel" in request.POST:
				preview = False
		if "submit" in request.POST:
			if form.is_valid():
				recomm = form.save(commit=False)
				recomm.user = request.user
				recomm.residence_quarter = request.user.profile.residence
				recomm.save()
				messages.success(request, "Document Soumis avec Succes ! ")
				return redirect(BASE_NAME+"_payform", recomm.id)
			return render(request, self.template_name, locals())
		if form.is_valid():
			recomm = form.save(commit=False)
			recomm.user = request.user
			recomm.residence_quarter = request.user.profile.residence
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


class DocumentDeleteView(LoginRequiredMixin, View):
	template_name = PREFIX_DOC_TEMP+'_del.html'

	def get(self, request, document_id, *args, **kwargs):
		delete = BASE_NAME+'_delete'
		document = Document.objects.get(id=document_id)
		return render(request, self.template_name, locals())

	def post(self, request, document_id, *args, **kwargs):
		delete = BASE_NAME+'_delete'
		document = Document.objects.get(id=document_id)

		if "oui" in request.POST:
			document.delete()
			messages.success(request, "Document Supprimé avec Succes ! ")
			return redirect(BASE_NAME+'_list')

		if "non" in request.POST:
			return redirect(BASE_NAME+'_list')

		return render(request, self.template_name, locals())

@login_required(login_url='/login/')
def delete_doc(request, document_id):
	delete = delete = BASE_NAME+'_delete'
	document = Document.objects.get(id=document_id)
	if request.user == document.user:
		document.delete()
		messages.success(request, "Document Supprimé avec Succes ! ")
	else:
		messages.error(request, "Vous avez pas le droit !")
	return redirect(BASE_NAME+'_list')

@login_required(login_url='/login/')
def update_doc(request, document_id):
	template_name = PREFIX_DOC_TEMP+"_form.html"
	update = BASE_NAME+'_update'
	document = Document.objects.get(id=document_id)
	form = DocumentForm(request.POST, request.FILES, instance =  document)
	if request.user == document.user:
		if(request.method == 'POST'):
			if form.is_valid():
				form.save()
				messages.success(request, "Document mis à jour avec Succes ! ")
				return redirect(BASE_NAME+'_list')
			else:
				messages.error(request, "Vous avez pas le droit !")
	form = DocumentForm(instance=document)
	return render(request, template_name, locals())


@login_required(login_url='/login/')
def clone_doc(request, document_id):
	clone = BASE_NAME+'_clone'
	document = Document.objects.get(id=document_id)
	if request.user == document.user:
		cloned_doc = document
		cloned_doc.pk = None
		cloned_doc.zone_payment =None
		cloned_doc.ready = False
		cloned_doc.secretary_validated = None
		cloned_doc.save()
		messages.success(request, "Document Cloné avec Succes ! ")
	else:
		messages.error(request, "Vous avez pas le droit !")
	return redirect(BASE_NAME+'_list')

