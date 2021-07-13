import hashlib

from django.shortcuts import render
from django.http import JsonResponse

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import parsers

from patients.models import Patient, User
from .serializers import PatientSerializer


@api_view(['GET'])
def apiOverview(request):
    api_urls = {
        'get-patient': '/get-patient/<str:pk>',
        'get-token': 'get-token'
    }
    return Response(api_urls)


@api_view(['GET'])
def getPatient(request, pk):
    user_token = request.headers['token']
    if User.objects.filter(token=user_token).exists():
        patients = Patient.objects.get(uuid=pk)
        serializer = PatientSerializer(patients, many=False)
        return Response(serializer.data)
    else:
        return JsonResponse(status=401)


@api_view(['GET'])
def getToken(request):
    user_login = request.headers['login']
    user_password = request.headers['password']

    if User.objects.filter(login=user_login, password_hash=hashlib.sha256(user_password.encode('utf-8')).hexdigest()).exists():
        u = User.objects.filter(login=user_login, password_hash=hashlib.sha256(user_password.encode('utf-8')).hexdigest()).first()
        print(hashlib.sha256(user_password.encode('utf-8')).hexdigest())
        return JsonResponse(
            {
                'token': u.token
            }
        )
    else:
        return JsonResponse({}, status=401)
