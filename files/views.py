from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    return render(request, 'files/index.html')

data = [
    {'name': 'image1.jpg', 'type':'jpg'},
    {'name': 'notes.txt', 'type': 'txt'},
    {'name': 'image2.jpg', 'type': 'jpg'}
]


def files(request):
    return render(request, 'files/files.html')