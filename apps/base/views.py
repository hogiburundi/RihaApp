import os, importlib

from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth import login, logout, authenticate 
from django.contrib import messages

from .forms import *
from .models import *

base_dir = os.path.split(os.path.relpath(__file__))[0]
MODULES = []

for directory in os.listdir('apps'):
	directory = os.path.join('apps', directory)
	if directory != base_dir:
		if os.path.exists(os.path.join(directory, "views.py")):
			views = os.path.join(directory, "views")
		elif os.path.exists(os.path.join(directory, os.path.join("views", "__init__.py"))):
			views = os.path.join(directory, "views")
		else:
			continue

		if os.path.exists(os.path.join(directory, "models.py")):
			models = os.path.join(directory, "models")
		elif os.path.exists(os.path.join(directory, os.path.join("models", "__init__.py"))):
			models = os.path.join(directory, "models")
		else:
			continue

		if os.path.exists(os.path.join(directory, "urls.py")):
			urls = os.path.join(directory, "urls")
		elif os.path.exists(os.path.join(directory, os.path.join("urls", "__init__.py"))):
			urls = os.path.join(directory, "urls")
		else:
			continue

		MODULES.append(directory, )

class Home(View):
	template_name = "index.html"

	def get(self, request, *args, **kwargs):
		if request.user.is_authenticated:
			all_docs = [os.path.basename(directory)+"_form" for directory in MODULES]
			return render(request, self.template_name, locals())
		else:
			return redirect("login")

class Secretariat(View):
	template_name = "secretariat.html"

	def get(self, request, *args, **kwargs):
		all_docs = []
		for directory in MODULES:
			models = os.path.join(directory, "models")
			models = importlib.import_module(models.replace(os.sep, '.'))
			counts = models.Document.objects.filter(
				secretary_validated=False,
				zone__leader=request.user).count()
			base_name = os.path.basename(directory)
			all_docs.append((base_name+"_secr_list", counts))

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
		form = RegisterForm(request.POST, request.FILES)
		if form.is_valid():
			try:
				username = form.cleaned_data['username']
				firstname = form.cleaned_data['firstname']
				lastname = form.cleaned_data['lastname']
				password = form.cleaned_data['password']
				avatar = form.cleaned_data['avatar']
				nationnalite = form.cleaned_data['nationnalite']
				quarter = form.cleaned_data['quarter']
				address = form.cleaned_data['address']
				CNI = form.cleaned_data['CNI']
				father = form.cleaned_data['father']
				mother = form.cleaned_data['mother']
				birthdate = form.cleaned_data['birthdate']
				is_married = form.cleaned_data['is_married']
				job = form.cleaned_data['job']
				user = User.objects.create_user(
					username=username,
					password=password)
				user.first_name, user.last_name = firstname, lastname
				user.save()
				Profile(user=user,
						avatar=avatar,
						nationnalite = nationnalite,
						quarter = quarter, 
						address = address, 
						CNI = CNI, 
						father = father, 
						mother = mother, 
						birthdate = birthdate, 
						is_married = is_married, 
						job = job
						).save()
				messages.success(request, "Hello "+username+", youn are registered successfully!")
				if user:
					login(request, user)
					return redirect("home")
			except Exception as e:
				print(str(e))
				messages.error(request, str(e))
		return render(request, self.template_name, locals())
