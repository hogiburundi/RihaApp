import os
from django.http import HttpResponseRedirect
from django.views.generic import CreateView
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import View
from django.db import transaction
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


class DocumentView(LoginRequiredMixin, View):
	template_name = "composition_form.html"
	heading_message = 'Attestation de Composition Familliale'
	
	def get(self, request, *args, **kwargs):

		form = DocumentForm()
		formset = ChildFormset()
		return render(request, self.template_name,  {'form':form,'formset' :formset})

	def post(self, request, *args, **kwargs):

		form = DocumentForm(request.POST)
		formset = ChildFormset(request.POST)
		if "preview" in request.POST:
			preview = True
		if "cancel" in request.POST:
			preview = False
		if "submit" in request.POST:
			if form.is_valid() and formset.is_valid():
				composition = form.save(commit=False)
				composition = formset.save(commit=False)
				composition.user = request.user

				for form in formset:
					child = form.save()
					child.composition = composition
					child.save()
					child.user = request.user
				return redirect("home")
			return render(request, self.template_name,  {'child':form,'composition' :formset})
		# if form.is_valid() and formset.is_valid():
		
		# 	composition = form.save()
		# 	child = formset.save()
		# 	composition.user = request.user
		# return render(request, self.template_name, locals())


	def get_context_data(self, **kwargs):
		data = super(DocumentView, self).get_context_data(**kwargs)
		if self.request.POST:
			data['child'] = ChildFormset(self.request.POST)
		else:
			data['child'] = ChildFormset()
		return data

	def form_valid(self, form, formset):
		context = self.get_context_data()
		child = context['child']
		with transaction.atomic():
			self.object = form.save()

			if child.is_valid():
				child.instance = self.object
				child.save()
			return super(DocumentView, self).form_valid(form)









# class DocumentView(LoginRequiredMixin, CreateView):
#     template_name = 'composition_form.html'
#     model = Document
#     form_class = DocumentForm
#     success_url = 'success/'

#     def get(self, request, *args, **kwargs):
#         """
#         Handles GET requests and instantiates blank versions of the form
#         and its inline formsets.
#         """
#         self.object = None
#         form_class = self.get_form_class()
#         # form = self.get_form(form_class)
#         form = DocumentForm(self.request.POST)
#         formset = ChildFormset()
#         # instruction_form = InstructionFormSet()
#         return render(request, self.template_name, {'form':form,'formset' :formset})

#     def post(self, request, *args, **kwargs):
#         """
#         Handles POST requests, instantiating a form instance and its inline
#         formsets with the passed POST variables and then checking them for
#         validity.
#         """
#         self.object = None
#         form_class = self.get_form_class()
#         form = DocumentForm(self.request.POST)
#         formset  = ChildFormset(self.request.POST)
#         # instruction_form = InstructionFormSet(self.request.POST)
#         if "preview" in request.POST:
#             preview = True
#         if "cancel" in request.POST:
#             preview = False
#         if "submit" in request.POST:
#             if form.is_valid() and formset.is_valid():
#                 composition = form.save(commit=False)
#                 for form in formset:
#                     child = form.save()
#                     child.composition = composition
#                     child.save()
#                     child.user = request.user
#                 return redirect("home")
#             return render(request, self.template_name, locals())
#         if form.is_valid() and formset.is_valid():
		
#             composition = form.save()
#             child = formset.save()
#             composition.user = request.user
#         return render(request, self.template_name, locals())

#         # if (form.is_valid() and formset .is_valid()): #and instruction_form.is_valid()):
#         #     return self.form_valid(form, formset)
#         # else:
#         #     return self.form_invalid(form, formset )

#     def form_valid(self, form, formset ):
#         """
#         Called if all forms are valid. Creates a Recipe instance along with
#         associated Ingredients and Instructions and then redirects to a
#         success page.
#         """
#         self.object = form.save()
#         formset .instance = self.object
#         formset .save(commit = True)
#         # instruction_form.instance = self.object
#         # instruction_form.save()
#         return HttpResponseRedirect(self.get_success_url())

#     def form_invalid(self, form, formset):
#         """
#         Called if a form is invalid. Re-renders the context data with the
#         data-filled forms and errors.
#         """
#         return render({'form' : form,'formset' : formset})

















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




