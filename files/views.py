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

@api_view(['GET'])
def files(request, format=None):
    data = File.objects.all()
    serializer = FileSerializer(data, many=True)
    return Response({'files': serializer.data})

@api_view(['GET', 'PATCH', 'DELETE'])
def file(request, file_id, format=None):
    try:
        data = File.objects.get(pk=file_id)
    except File.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method == 'GET':
        serializer = FileSerializer(data)
        return Response({'file': serializer.data})

    elif request.method == 'PATCH':
        serializer = FileSerializer(data, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        data.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)