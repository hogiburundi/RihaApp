import os
from django.http import HttpResponseRedirect
from django.views.generic import CreateView
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import View
from django.forms import formset_factory

from .forms import *
from apps.base.forms import *
from .models import *

BASE_NAME = os.path.split(os.path.split(os.path.abspath(__file__))[0])[1]

class SecretaryListView(LoginRequiredMixin, View):
	template_name = "composition_secr_list.html"
	def get(self, request, document_id=None, *args, **kwargs):
		documents = Document.objects.all()
		return render(request, self.template_name, locals())

class SecretaryView(LoginRequiredMixin, View):
	template_name = "composition_secr_edit.html"

	def get(self, request, document_id, *args, **kwargs):
		composition = get_object_or_404(Document, id=document_id)
		return render(request, self.template_name, locals())

	def post(self, request, document_id, *args, **kwargs):
		composition = get_object_or_404(Document, id=document_id)
		if "reject" in request.POST:
			composition.rejection_msg = request.POST["rejection_msg"]
			composition.secretary_validated = True
			composition.save()
			return redirect(BASE_NAME+'_secr_list')

		if "cancel" in request.POST:
			pass
		if "validate" in request.POST:
			composition.secretary_validated = True
			composition.save()
			return redirect(BASE_NAME+'_secr_list')
		return render(request, self.template_name, locals())

class DocumentListView(LoginRequiredMixin, View):
	template_name = "composition_list.html"
	def get(self, request, document_id=None, *args, **kwargs):
		formurl = BASE_NAME+"_form"
		payform = BASE_NAME+"_payform"
		documents = Document.objects.filter(user=request.user)
		print(documents)
		return render(request, self.template_name, locals())

class DocumentPayView(LoginRequiredMixin, View):
	template_name = "composition_pay_form.html"

	def get(self, request, composition, *args, **kwargs):
		payform = BASE_NAME+"_payform"
		document = Document.objects.get(id=composition)
		if document.zone_payment:
			return redirect(BASE_NAME+"_list")
		form = PaymentZoneForm()
		return render(request, self.template_name, locals())

	def post(self, request, composition, *args, **kwargs):
		payform = BASE_NAME+"_payform"
		document = Document.objects.get(id=composition)
		form = PaymentZoneForm(request.POST, request.FILES)
		if form.is_valid():
			zone_payment = form.save(commit=False)
			zone_payment.place = document.zone
			zone_payment.save()
			document.zone_payment = zone_payment
			document.save()
			return redirect(BASE_NAME+"_list")
		return render(request, self.template_name, locals())


class DocumentView(LoginRequiredMixin, View):
	template_name = "composition_form.html"
	heading_message = 'Attestation de Composition Familliale'

	def get(self, request, *args, **kwargs):
		children = Child.childrenOf(request.user.profile)
		form_set=formset_factory(ChildForm)
		form = DocumentForm(initial = {'quarter': request.user.profile.residence })
		return render(request, self.template_name, locals())

	def post(self, request, *args, **kwargs):
		children = Child.childrenOf(request.user.profile)
		form = DocumentForm(request.POST)
		form_set=formset_factory(ChildForm)
		if "preview" in request.POST:
			preview = True
		if "cancel" in request.POST:
			preview = False
		if "submit" in request.POST:
			if form.is_valid():
				composition = form.save(commit=False)
				composition.user = request.user
				composition.save()
				formset=form_set(request.POST)
				if formset.is_valid():
					for childform in formset:
						child = childform.save(commit=False)
						print(child.date)
						this = request.user.profile
						child.mother = this if this.gender == "F" else composition.conjoint
						child.father = this if this.gender == "H" else composition.conjoint
						child.save()
				return redirect(BASE_NAME+"_payform", composition=composition.id)
		if form.is_valid():
			composition = form.save(commit=False)
			composition.user = request.user
		return render(request, self.template_name, locals())

class DocumentChildView(LoginRequiredMixin, View):
	template_name = 'child_form.html'
	documents = Document.objects.all()

	def get(self, request, pk,*args, **kwargs):
		documents = Document.objects.get(id=pk)
		form = ChildForm(queryset=Document.objects.filter(user=request.user),instance=documents)

		return render(request, self.template_name, locals())

	def post(self, request, *args, **kwargs):
		form = ChildForm(request.POST)
		if form.is_valid():
			formset = form.save(commit=False)
			formset.user = request.user
			formset.save()
			return redirect(BASE_NAME+"_form")
		return render(request, self.template_name, locals())
		if form.is_valid():
			formset = form.save(commit=False)
			formset.user = request.user
		return render(request, self.template_name, locals())
