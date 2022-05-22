from django.http import Http404, JsonResponse
from django.shortcuts import redirect, render

from files.forms import UploadForm
from files.serializers import FileSerializer, UserSerializer
from .models import File

from django.conf import settings

from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes

from rest_framework.permissions import IsAuthenticated


def index(request):
    return render(request, 'files/index.html')

@api_view(['GET', 'POST'])
@permission_classes([IsAuthenticated])
def files(request, format=None):
    if request.method == 'GET':
        data = request.user.file_set.all()
        #data = File.objects.all()
        serializer = FileSerializer(data, many=True)
        return Response({'files': serializer.data})
    
    elif request.method == 'POST':
        serializer = FileSerializer(data=request.data, context={'request': request})
        print(request.data)
        if serializer.is_valid():
            settings.AWS_S3_OBJECT_PARAMETERS = {'CacheControl': 'max-age=86400', 
			'ContentDisposition': 'attachment; filename="' + request.FILES['file'].name + '"'}
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PATCH', 'DELETE'])
@permission_classes([IsAuthenticated])
def file(request, file_id, format=None):
    try:
        data = request.user.file_set.get(pk=file_id)
        #data = File.objects.get(pk=file_id)
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

@api_view(['POST'])
def register(request):
    serializer = UserSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(status=status.HTTP_201_CREATED)