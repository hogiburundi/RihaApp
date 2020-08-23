import os
from django.urls import path
from . import views

BASE_NAME = os.path.split(os.path.split(os.path.abspath(__file__))[0])[1]

urlpatterns = [
    path('', views.DocumentListView.as_view(), name=BASE_NAME+"_list"),
    path('form/', views.DocumentFormView.as_view(), name=BASE_NAME+"_form"),
    path('payform/<acte_reconnais>', views.DocumentPayView.as_view(), name=BASE_NAME+"_payform"),
    path('secretary/', views.SecretaryListView.as_view(), name=BASE_NAME+'_secr_list'),
    path('secretary/<document_id>', views.SecretaryView.as_view(), name=BASE_NAME + '_secr_edit'),
    path('secretary/pay/<document_id>', views.SecretaryPayView.as_view(), name=BASE_NAME + '_secr_pay'),
    path('update_acrec/<document_id>/<usid>', views.update_AcRec_Document, name="update_acrec"),
    path('delete_acrec/<document_id>/<usid>', views.delete_AcRec_Document, name="delete_acrec"),
]
