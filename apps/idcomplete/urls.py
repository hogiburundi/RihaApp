import os
from django.urls import path
from . import views

BASE_NAME = os.path.split(os.path.split(os.path.abspath(__file__))[0])[1]

urlpatterns = [
    path('', views.DocumentView.as_view(), name=BASE_NAME+"_form"),
    path('secretary/', views.SecretaryListView.as_view(), name=BASE_NAME+'_secr_list'),
    path('secretary/<document_id>', views.SecretaryView.as_view(), name=BASE_NAME+'_secr_edit'),
]
