from django.urls import path
from . import views

urlpatterns = [
	path("", views.Home.as_view(), name='home'),
	path("secretariat", views.Secretariat.as_view(), name='secretariat'),
	path("login/", views.Connexion.as_view(), name='login'),
	path("logout/", views.disconnect, name='logout'),
	path("register/", views.Register.as_view(), name='register'),
	path("register2/", views.Register2.as_view(), name='register2'),
	path("profile-form/", views.ProfileView.as_view(), name='profile_form'),
	path("verifier-cni/", views.verifierCni, name='verifier_cni'),
	path("addUser/", views.AddUser, name='addUser'),
]
