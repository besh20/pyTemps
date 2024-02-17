from django.shortcuts import render, HttpResponse
from .models import *
# Create your views here.

def home(request):

    desc = company.objects.all().first()
    data_desc = {
        'desc': desc
        }
    return render (request, "index.html", data_desc)

def prod(request):
    desc = company.objects.all().first()
    prod_info = products.objects.all()
    data_prod_info ={
        'desc': desc,
        'prod_info': prod_info
    }
    return render (request, "products.html", data_prod_info)


def contact(request):
    desc = company.objects.all().first()
    data_desc = {
        'desc': desc
        }
    return render (request, "contact.html", data_desc)

def about(request):
    desc = company.objects.all().first()
    data_desc = {
        'desc': desc
        }
    return render (request, "about.html",data_desc)
