import os, importlib

from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth import login, logout, authenticate 
from django.contrib import messages

from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import user_passes_test

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
			profile = Profile.objects.filter(user=request.user)
			home_urls = []
			for directory in MODULES:
				basename = os.path.basename(directory)
				module_name = directory.replace(os.sep, ".")
				module = importlib.import_module(module_name)
				app_name = module.APP_NAME
				home_urls.append((app_name, basename+"_list"))
			return render(request, self.template_name, locals())
		else:
			return redirect("login")

# @method_decorator(user_passes_test(lambda u: u.is_superuser), name='dispatch')
class Secretariat(View):
	template_name = "secretariat.html"

	def get(self, request, *args, **kwargs):
		home_urls = []
		
		if not (request.user.is_authenticated):return redirect("login")

		for directory in MODULES:
			models = os.path.join(directory, "models")
			models = importlib.import_module(models.replace(os.sep, '.'))
			#=============================================================
			# counts = models.Document.objects.filter(
			# 	secretary_validated=False,
			# 	zone__leader=request.user).count()
			counts = models.Document.objects.filter(secretary_validated__isnull=True, ).count()
			#=============================================================
			basename = os.path.basename(directory)
			module_name = directory.replace(os.sep, ".")
			module = importlib.import_module(module_name)
			app_name = module.APP_NAME
			home_urls.append((app_name, basename+"_secr_list", counts))#counts))

		return render(request, self.template_name, locals())

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
	page_number = 1

	def get(self, request, *args, **kwargs):
		page_number = self.page_number
		form = RegisterForm()
		return render(request, self.template_name, locals())

	def post(self, request, *args, **kwargs):
		quarters = Quarter.objects.all()
		page_number = self.page_number
		form = RegisterForm(request.POST)
		if form.is_valid():
			try:
				username = form.cleaned_data['telephone']
				firstname = form.cleaned_data['firstname']
				lastname = form.cleaned_data['lastname']
				password = form.cleaned_data['password']
				user = User.objects.create_user(
					username=username,
					password=password)
				user.first_name, user.last_name = firstname, lastname
				user.save()
				profile = Profile(user=user)
				profile.save()
				messages.success(request, "Hello "+username+", you are registered successfully!")
				if user:
					login(request, user)
					return redirect("profile_form")
			except Exception as e:
				messages.error(request, str(e))
		return render(request, self.template_name, locals())

class ProfileView(View):
	template_name = 'form.html'
	next_p = "register2"
	page_number = 2

	def get(self, request, *args, **kwargs):
		quarters = Quarter.objects.all()
		try:
			next_ = request.GET["next"]
			self.next_p = next_ if next_ else self.next_p
		except:
			print
		page_number = self.page_number
		profile = Profile.objects.get_or_create(user=request.user)[0]
		form = ProfileForm(instance=profile)
		return render(request, self.template_name, locals())

	def post(self, request, *args, **kwargs):
		quarters = Quarter.objects.all()
		profile = Profile.objects.get_or_create(user=request.user)[0]
		form = ProfileForm(request.POST, instance=profile)
		page_number = self.page_number
		if form.is_valid():
			try:
				profile = form.save(commit=False)
				profile.user = request.user
				profile.save()
				messages.success(request, "Hello "+request.user.first_name+", your profile created successfully!")
				return redirect(self.next_p)
			except Exception as e:
				messages.error(request, str(e))
		return render(request, self.template_name, locals())

class Register2(View):
	template_name = 'form.html'
	next_p = "home"
	page_number = 3

	def get(self, request, *args, **kwargs):
		form = Register2Form()
		page_number = self.page_number
		try:
			self.next_p = request.GET["next"]
		except:
			print
		return render(request, self.template_name, locals())

	def post(self, request, *args, **kwargs):
		form = Register2Form(request.POST, request.FILES)
		page_number = self.page_number
		if form.is_valid():
			form.save()
			messages.success(request, "Hello "+request.user.first_name+", you are registered successfully!")
			return redirect(self.next_p)
		return render(request, self.template_name, locals())
