from django.shortcuts import render
from django.http import HttpResponse, HttpRequest


# Create your views here.
def all_blogs(request: HttpRequest):
    return HttpResponse("Hello World")
