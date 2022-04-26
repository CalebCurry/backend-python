from django.http import Http404, JsonResponse
from django.shortcuts import redirect, render

from files.forms import UploadForm
from files.serializers import FileSerializer
from .models import File

from django.conf import settings

def index(request):
    return render(request, 'files/index.html')

def files(request):
    data = File.objects.all()
    serializer = FileSerializer(data, many=True)
    return JsonResponse({'files': serializer.data})