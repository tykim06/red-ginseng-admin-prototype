from django.urls import path
from . import views

app_name='customer'
urlpatterns = [
    path('upload/', views.upload, name='upload'),
    path('sms/', views.sms, name='sms'),
    path('', views.index, name='index'),
]
