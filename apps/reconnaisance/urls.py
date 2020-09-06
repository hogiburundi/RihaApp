import os
from django.urls import path
from . import views

BASE_NAME = os.path.split(os.path.split(os.path.abspath(__file__))[0])[1]

urlpatterns = [
    path('', views.DocumentListView.as_view(), name=BASE_NAME+"_list"),
    path('form/', views.DocumentFormView.as_view(), name=BASE_NAME+"_form"),
    path('payform/<reconnais>', views.DocumentPayView.as_view(), name=BASE_NAME+"_payform"),
    path('secretary/', views.SecretaryListView.as_view(), name=BASE_NAME+'_secr_list'),
    path('secretary/<document_id>', views.SecretaryView.as_view(), name=BASE_NAME + '_secr_edit'),
    path('secretary/pay/<document_id>', views.SecretaryPayView.as_view(), name=BASE_NAME + '_secr_pay'),
    path('update_att_rec/<document_id>/<usid>', views.update_Att_Rec_Document, name="update_att_rec"),
    path('delete_att_rec/<document_id>/<usid>', views.delete_Att_Rec_Document, name="delete_att_rec"),
    path('clone_att_rec/<document_id>/<usid>', views.clone_Att_Rec_Document, name="clone_att_rec"),
]
