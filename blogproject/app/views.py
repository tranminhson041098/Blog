from django.shortcuts import render
from django.shortcuts import HttpResponse

# Create your views here.

def hello(request):
    response = HttpResponse("Hello app")
    return response
