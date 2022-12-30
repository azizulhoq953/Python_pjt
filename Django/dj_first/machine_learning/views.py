from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def mlearning(htrequest):
    return HttpResponse(" <h1> Hello Sir Your First HttpRequest Successfully Run </h1> ")

def Dlearning(htrequest):
    return HttpResponse("y're Welcome I'ts a Second Function And Second URl Define Successful")