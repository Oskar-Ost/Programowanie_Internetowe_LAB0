from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def home(request):
    return HttpResponse("Moje hobby to Fotografia!")

def about(request):
    return HttpResponse("Kilka słów o moim hobby")

def gallery(request):
    return HttpResponse("Galeria zdjęć")