from django.urls import path
from . import views

app_name='customer'
urlpatterns = [
    path('upload/', views.upload, name='upload'),
    path('message/', views.message, name='message'),
    path('', views.index, name='index'),
]
