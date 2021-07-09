from django.shortcuts import render
from django.http import HttpResponse
from .forms import PatientForm


# Get response with list of all patients.
def plist(request):
    return render(request, 'patients/list.html')


# Get response with patient add menu.
def add(request):
    form = PatientForm()
    if request.method == 'POST':
        print(request.POST)
        form = PatientForm(request.POST)
        print(form.is_valid())
        if form.is_valid():
            form.save()
    context = {'form': form}
    return render(request, 'patients/add.html', context)
