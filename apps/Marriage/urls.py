import os
from django.urls import path
from . import views

BASE_NAME = os.path.split(os.path.split(os.path.abspath(__file__))[0])[1]

urlpatterns = [
    path('', views.DocumentListView.as_view(), name=BASE_NAME+"_list"),
    path('form/', views.DocumentFormView.as_view(), name=BASE_NAME+"_form"),
    path('payform/<marriage>', views.DocumentPayView.as_view(), name=BASE_NAME+"_payform"),
    path('secretary/', views.SecretaryListView.as_view(), name=BASE_NAME+'_secr_list'),
    path('secretary/pay/<document_id>', views.SecretaryPayView.as_view(), name=BASE_NAME+'_secr_pay'),
    path('secretary/<document_id>', views.SecretaryView.as_view(), name=BASE_NAME+'_secr_edit'),
    path('update/<id>', views.update_document, name=BASE_NAME+'_secr_list'),
    path('delete/<document_id>', views.delete_document, name = "delete"),
    path('clone/<document_id>', views.clone_doc, name = "clone"),
    
]

