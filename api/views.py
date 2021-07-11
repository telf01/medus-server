from django.shortcuts import render
from django.http import JsonResponse

from rest_framework.decorators import api_view
from rest_framework.response import Response

from patients.models import Patient
from .serializers import PatientSerializer


@api_view(['GET'])
def apiOverview(request):
    api_urls = {
        'patient': '/patient-get/<str:pk>'
    }
    return Response(api_urls)


@api_view(['GET'])
def getPatient(request, pk):
    patients = Patient.objects.get(uuid=pk)
    serializer = PatientSerializer(patients, many=False)
    return Response(serializer.data)
