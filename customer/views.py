from django.shortcuts import render
from django.http import HttpResponse
from tablib import Dataset
from .resources import CustomerResource

from .models import Customer

# Create your views here.
def index(req):
    customers = Customer.objects.all()
    return render(req, 'index.html', {'customers' : customers})

def upload(req):
    if req.method == 'GET':
        return render(req, 'upload.html');
    elif req.method == 'POST':
        customer_resource = CustomerResource()
        dataset = Dataset()
        myfile = req.FILES['myfile']

        data = dataset.load(myfile.read())
        result = customer_resource.import_data(dataset, dry_run=True)  # Test the data import

        if not result.has_errors():
            customer_resource.import_data(dataset, dry_run=False)  # Actually import now
        return render(req, 'confirm.html', {'result' : "Excel Upload Done!"})

def sms(req):
    if req.method == 'GET':
        return render(req, 'sms.html');
    elif req.method == 'POST':
        return render(req, 'confirm.html', {'result' : "Sending SMS Done!"})
