from django.urls import path
from . import views

urlpatterns = [
    path('', views.IdCompleteView.as_view(), name='idcomplete'),
    path('confirm', views.Confirmation.as_view(), name='confirm'),
    path('confirm/<idcomplete>', views.Confirmation.as_view(), name='confirm'),
]
