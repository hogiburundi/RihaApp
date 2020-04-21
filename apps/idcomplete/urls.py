from django.urls import path
from . import views

urlpatterns = [
    path('', views.IdCompleteView.as_view(), name='idcomplete')
]
