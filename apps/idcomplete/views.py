from django.shortcuts import render, redirect
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import View
from .forms import IdCompleteForm
from .models import *

class IdCompleteView(LoginRequiredMixin, View):
	template_name = "idcomp_form.html"
	quarters = Quarter.objects.all()
	zones = Zone.objects.all()

	def get(self, request, *args, **kwargs):
		quarters = self.quarters 
		zones = self.zones 
		form = IdCompleteForm()
		return render(request, self.template_name, locals())

	def post(self, request, *args, **kwargs):
		quarters = self.quarters 
		zones = self.zones 
		form = IdCompleteForm(request.POST)
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

class Confirmation(View):
	template_name = "idcomp_confirm.html"

	def get(self, request, id_compl, *args, **kwargs):
		return render(request, self.template_name, locals())

	def post(self, request, *args, **kwargs):
		if "continue" in request:
			id_compl = request.get['id_compl']
			id_compl.save()
			print("continue", id_compl)
			return redirect("home")
		if "cancel" in request:
			print("cancel")
			return redirect("idcomplete")
		return render(request, self.template_name, locals())

