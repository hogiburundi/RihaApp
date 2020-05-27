import os

from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import View

from .forms import DocumentForm
from .models import *

BASE_NAME = os.path.split(os.path.split(os.path.abspath(__file__))[0])[1]

class SecretaryListView(LoginRequiredMixin, View):
	template_name = "idcomp_secr_list.html"
	def get(self, request, document_id=None, *args, **kwargs):
		documents = Document.objects.all()
		return render(request, self.template_name, locals())

class SecretaryView(LoginRequiredMixin, View):
	template_name = "idcomp_secr_edit.html"

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

class DocumentView(LoginRequiredMixin, View):
	template_name = "idcomp_form.html"
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
				id_compl = form.save(commit=False)
				id_compl.user = request.user
				id_compl.save()
				return redirect("home")
			return render(request, self.template_name, locals())
		if form.is_valid():
			id_compl = form.save(commit=False)
			id_compl.user = request.user
		return render(request, self.template_name, locals())

