from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth import login, logout, authenticate 
from django.contrib import messages

from .forms import *

class Home(View):
	template_name = "index.html"

	def get(self, request, *args, **kwargs):
		if request.user.is_authenticated:
			return render(request, self.template_name, locals())
		else:
			return redirect("login")

def disconnect(request):
	show_hidden = "hidden"
	logout(request)
	return redirect("login")


class Connexion(View):
	template_name = 'login.html'
	next_p = "home"

	def get(self, request, *args, **kwargs):
		form = ConnexionForm()
		try:
			self.next_p = request.GET["next"]
		except:
			print
		return render(request, self.template_name, locals())

	def post(self, request, *args, **kwargs):
		form = ConnexionForm(request.POST)
		if form.is_valid():
			username = form.cleaned_data['username']
			password = form.cleaned_data['password']
			user = authenticate(username=username, password=password)
			if user:  # Si l'objet renvoyé n'est pas None
				login(request, user)
				messages.success(request, "You're now connected!")
				return redirect(self.next_p)
			else:
				messages.error(request, "logins incorrect!")
		return render(request, self.template_name, locals())

class Register(View):
	template_name = 'register.html'
	next_p = "home"

	def get(self, request, *args, **kwargs):
		quarters = Quarter.objects.all()
		form = RegisterForm()
		try:
			self.next_p = request.GET["next"]
		except:
			print
		return render(request, self.template_name, locals())

	def post(self, request, *args, **kwargs):
		quarters = Quarter.objects.all()
		form = ConnexionForm(request.POST)
		if form.is_valid():
			username = form.cleaned_data['username']
			password = form.cleaned_data['password']
			user = authenticate(username=username, password=password)
			if user:  # Si l'objet renvoyé n'est pas None
				login(request, user)
				messages.success(request, "You're now connected!")
				return redirect(self.next_p)
			else:
				messages.error(request, "logins incorrect!")
		return render(request, self.template_name, locals())
