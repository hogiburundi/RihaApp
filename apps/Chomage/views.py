import os

from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import View
from django.contrib import messages
from .forms import *
from apps.base.forms import *
from .models import *

BASE_NAME = os.path.split(os.path.split(os.path.abspath(__file__))[0])[1]

class SecretaryListView(LoginRequiredMixin, View):
	template_name = "chomage_secr_list.html"
	def get(self, request, document_id=None, *args, **kwargs):
		documents = Document.objects.all()
		# documents = Document.onlyPaid()
		return render(request, self.template_name, locals())

class SecretaryView(LoginRequiredMixin, View):
	template_name = "chomage_secr_edit.html"

	def get(self, request, document_id, *args, **kwargs):
		validation_form = ValidationForm()
		chomage = get_object_or_404(Document, id=document_id)
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
				notification += " ".join([x for x in Document.requirements()])
				Notification(user=document.user, message=notification).save()
				return redirect(BASE_NAME+"_secr_list")

			if "valid" in request.POST:
				document.secretary_validated = True
				document.save()
				return redirect(BASE_NAME+'_secr_list')
		return render(request, self.template_name, locals())


class SecretaryPayView(LoginRequiredMixin, View):
	template_name = "chomage_secr_pay.html"

	def get(self, request, document_id, *args, **kwargs):
		modal_mode = False
		abandon = get_object_or_404(Document, id=document_id)
		return render(request, self.template_name, locals())


class DocumentListView(LoginRequiredMixin, View):
	template_name = "chomage_list.html"
	def get(self, request, document_id=None, *args, **kwargs):
		formurl = BASE_NAME+"_form"
		payform = BASE_NAME+"_payform"
		documents = Document.objects.filter(user=request.user)
		print(documents)
		return render(request, self.template_name, locals())

class DocumentFormView(LoginRequiredMixin, View):
	template_name = "chomage_form.html"

	def get(self, request, *args, **kwargs):
		form = DocumentForm()
		return render(request, self.template_name, locals())

	def post(self, request, *args, **kwargs):
		form = DocumentForm(request.POST)
		if "preview" in request.POST:
			preview = True
		if "cancel" in request.POST:
			preview = False
		if "submit" in request.POST:
			if form.is_valid():
				chomage = form.save(commit=False)
				chomage.user = request.user
				chomage.save()
				messages.success(request, "Document cree avec Succes ! ")
				return redirect(BASE_NAME+"_payform", chomage=chomage.id)
			return render(request, self.template_name, locals())
		if form.is_valid():
			chomage = form.save(commit=False)
			chomage.user = request.user
		return render(request, self.template_name, locals())


class DocumentPayView(LoginRequiredMixin, View):
	template_name = "chomage_pay_form.html"

	def get(self, request, chomage, *args, **kwargs):
		payform = BASE_NAME+"_payform"
		document = Document.objects.get(id=chomage)
		if document.zone_payment:
			return redirect(BASE_NAME+"_list")
		form = PaymentZoneForm()
		return render(request, self.template_name, locals())

	def post(self, request, chomage, *args, **kwargs):
		payform = BASE_NAME+"_payform"
		document = Document.objects.get(id=chomage)
		form = PaymentZoneForm(request.POST, request.FILES)
		if form.is_valid():
			zone_payment = form.save(commit=False)
			zone_payment.place = document.zone
			zone_payment.save()
			document.zone_payment = zone_payment
			document.save()
			return redirect(BASE_NAME+"_list")
		return render(request, self.template_name, locals())



def delete_document(request, document_id, template_name='chomage_delete_form.html'):
    form= get_object_or_404(Document, id=document_id)  
    if request.user == form.user:  
        if request.method=='POST':
            form.delete()
            messages.success(request, "Document supprimé avec Succes ! ")
            return redirect(BASE_NAME+"_list")
        return render(request, template_name, {'form':form})


def update_document(request, id): 
    context ={} 

    document = get_object_or_404(Document, id = id) 

    form1 = DocumentForm(request.POST or None, instance = document) 
    if request.user == document.user:
        if form1.is_valid():
            form = form1.save(commit = False)
            form.user = request.user
            form.save() 
            # messages.success(request, "Document modifie avec Succes ! ")
            return redirect(BASE_NAME+"_list")


    context["form"] = form1 
    return render(request, "chomage_update_form.html", context) 


def clone_doc(request, document_id):
	clone = BASE_NAME+'_clone'
	document = Document.objects.get(id=document_id)
	if request.user == document.user:
		cloned_doc = document
		cloned_doc.pk = None
		cloned_doc.ready = False
		cloned_doc.secretary_validated = None
		cloned_doc.save()
		messages.success(request, "Document Cloné avec Succes ! ")
	else:
		messages.error(request, "Vous avez pas le droit !")
	return redirect(BASE_NAME+'_list')

