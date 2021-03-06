import os
from django.urls import path
from . import views

BASE_NAME = os.path.split(os.path.split(os.path.abspath(__file__))[0])[1]

urlpatterns = [
    path('', views.DocumentListView.as_view(), name=BASE_NAME+"_list"),
    path('form/', views.DocumentFormView.as_view(), name=BASE_NAME+"_form"),
    path('payform/<cession>', views.DocumentPayView.as_view(), name=BASE_NAME+"_payform"),
    path('secretary/', views.SecretaryListView.as_view(), name=BASE_NAME+'_secr_list'),
    path('secretary/<document_id>', views.SecretaryView.as_view(), name=BASE_NAME + '_secr_edit'),
    path('secretary/pay/<document_id>', views.SecretaryPayView.as_view(), name=BASE_NAME + '_secr_pay'),
    path('update_cess/<document_id>/<usid>', views.update_Cess_Document, name="update_cess"),
    path('delete_cess/<document_id>/<usid>', views.delete_Cess_Document, name="delete_cess"),
    path('clone_cess/<document_id>/<usid>', views.clone_Cess_Document, name="clone_cess"),
]
