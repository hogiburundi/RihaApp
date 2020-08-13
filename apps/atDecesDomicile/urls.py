import os
from django.urls import path
from . import views

BASE_NAME = os.path.split(os.path.split(os.path.abspath(__file__))[0])[1]

urlpatterns = [
	path('', views.DocumentListView.as_view(), name=BASE_NAME+"_list"),
	path('form/', views.DocumentFormView.as_view(), name=BASE_NAME+"_form"),
	path('secretary/', views.SecretaryListView.as_view(), name=BASE_NAME+'_secr_list'),
	path('secretary/<document_id>', views.SecretaryView.as_view(), name=BASE_NAME+'_secr_edit'),
	path('delete/at_deces_dom/<document_id>', views.delete_doc, name=BASE_NAME+"_delconfirm"),
	path('update/at_deces_dom/<document_id>', views.update_doc, name=BASE_NAME+"_update"),
	path('clone/at_deces_dom/<document_id>', views.clone_doc, name=BASE_NAME+"_clone"),
	]
