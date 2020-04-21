from django.shortcuts import render, redirect
from django.views import View
from .forms import IdCompleteForm
from .models import *

class IdCompleteView(View):
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
		if form.is_valid():
			id_compl = form.save(commit=False)
			id_compl.user = request.user
			return render(request, "idcomp_confirm.html", locals())
		return render(request, self.template_name, locals())

class Confirmation(View):
	template_name = "idcomp_confirm.html"

	def get(self, request, *args, **kwargs):
		return render(request, self.template_name, locals())

	def post(self, request, *args, **kwargs):
		if "continue" in request:
			return redirect("home")
		if "cancel" in request:
			return redirect("idcomplete")
		return render(request, self.template_name, locals())

