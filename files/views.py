from django.http import Http404, JsonResponse
from django.shortcuts import redirect, render

from files.forms import UploadForm
from files.serializers import FileSerializer
from .models import File

from django.conf import settings

from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view


def index(request):
    return render(request, 'files/index.html')

def files(request, format=None):
    data = File.objects.all()
    serializer = FileSerializer(data, many=True)
    return JsonResponse({'files': serializer.data})

@api_view(['GET'])
def file(request, file_id, format=None):
    try:
        data = File.objects.get(pk=file_id)
    except File.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    serializer = FileSerializer(data)
    return Response({'file': serializer.data})