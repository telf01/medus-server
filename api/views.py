import hashlib
import json

from django.shortcuts import render
from django.http import JsonResponse
from django.core import serializers

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import parsers

from patients.models import Patient, User, Note
from .serializers import PatientSerializer, NoteSerializer


@api_view(['GET'])
def apiOverview(request):
    api_urls = {
        'get-patient': '/get-patient/<str:pk>',
        'get-token': '/get-token/',
        'add-note': '/add-note/',
        'get-notes': '/get-notes/'
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

@api_view(['GET'])
def addNote(request):
    user_token = request.headers['token']
    if User.objects.filter(token=user_token).exists():
        print(request.body)
        raw_data = json.loads(request.body)
        note = Note()
        note.header = raw_data['header']
        note.time_of_creation = raw_data['time_of_creation']
        note.text = raw_data['text']
        note.patient = Patient.objects.get(uuid=raw_data['uuid'])
        note.save()
        return JsonResponse({}, status=200)
    else:
        return JsonResponse({}, status=401)


@api_view(['GET'])
def getNotes(request, pk):
    user_token = request.headers['token']
    if User.objects.filter(token=user_token).exists():
        patient = Patient.objects.get(uuid=pk)
        notes = Note.objects.filter(patient=patient).all()
        js = NoteSerializer(notes, many=True)
        print(js.data)
        return JsonResponse({'note':js.data}, status=200)
    else:
        return JsonResponse({}, status=401)
