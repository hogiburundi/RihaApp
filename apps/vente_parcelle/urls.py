import os
from django.urls import path
from . import views

BASE_NAME = os.path.split(os.path.split(os.path.abspath(__file__))[0])[1]

urlpatterns = [
    path('', views.DocumentListView.as_view(), name=BASE_NAME+"_list"),
    path('form/', views.DocumentFormView.as_view(), name=BASE_NAME+"_form"),
    path('payform/<vente_parcelle>', views.DocumentPayView.as_view(), name=BASE_NAME+"_payform"),
    path('secretary/', views.SecretaryListView.as_view(), name=BASE_NAME+'_secr_list'),
    path('secretary/<document_id>', views.SecretaryView.as_view(), name=BASE_NAME + '_secr_edit'),
    path('secretary/pay/<document_id>', views.SecretaryPayView.as_view(), name=BASE_NAME + '_secr_pay'),
    path('update_vente/<document_id>/<usid>', views.update_Vente_Document, name="update_vente"),
    path('delete_vente/<document_id>/<usid>', views.delete_Vente_Document, name="delete_vente"),
    path('clone_vente/<document_id>/<usid>', views.clone_Vente_Document, name="clone_vente"),
]

