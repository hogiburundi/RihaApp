from django.urls import path
from . import views

urlpatterns = [
	path("", views.Home.as_view(), name='home'),
	path("secretariat", views.Secretariat.as_view(), name='secretariat'),
	path("login/", views.Connexion.as_view(), name='login'),
	path("logout/", views.disconnect, name='logout'),
	path("register/", views.Register.as_view(), name='register'),
]
