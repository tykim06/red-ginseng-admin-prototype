from django.shortcuts import render
from django.http import HttpResponse

from .models import Customer

# Create your views here.
def index(req):
    customers = Customer.objects.all()
    return render(req, 'index.html', {'customers' : customers})

def upload(req):
    if req.method == 'GET':
        return render(req, 'upload.html');
    elif req.method == 'POST':
        return render(req, 'confirm.html', {'result' : "Excel Upload Done!"})

def sms(req):
    if req.method == 'GET':
        return render(req, 'sms.html');
    elif req.method == 'POST':
        return render(req, 'confirm.html', {'result' : "Sending SMS Done!"})
