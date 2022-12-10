from  . import views
from django.urls import path

urlpatterns = [
path('access_token/', views.getAccessToken, name = 'access_token'),
path('mpesa-pay/', views.lipa_na_mpesa_online, name = 'mpesa-pay'),
path('lipa/', views.lipa, name = 'lipa'),
]
