from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


# Get response with list of all patients.
def plist(request):
    return render(request, 'patients/list.html')


# Get response with patient add menu.
def add(request):
    return render(request, 'patients/add.html')
