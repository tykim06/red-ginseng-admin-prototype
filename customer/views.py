from django.shortcuts import render
from django.http import HttpResponse
from .models import Customer

# Create your views here.
def index(req):
    customers = Customer.objects.all()
    return HttpResponse("hello world! this is customer index</br>"+', '.join([c.name for c in customers]))

def upload(req):
    return HttpResponse("upload!")

def list(req):
    return HttpResponse("list!")
