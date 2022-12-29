from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def mlearning(htrequest):
    return HttpResponse("Hello Sir Your First HttpRequest Successfully Run")
