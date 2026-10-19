from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def home(request):
    context = {
        "hobby_name": "Fotografia",
        "description": "Lubie fotografować",
    }
#    return HttpResponse("Moje hobby to Fotografia!")
    return render(request, 'hobby/home.html', context)

def about(request):
#    return HttpResponse("Kilka słów o moim hobby")
    return render(request, 'hobby/about.html')

def gallery(request):
#    return HttpResponse("Galeria zdjęć")
    return render(request, 'hobby/gallery.html')