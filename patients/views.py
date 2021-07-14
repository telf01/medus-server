from django.shortcuts import render
from django.http import HttpResponse
from .forms import PatientForm, UserForm
from .models import Patient

# Get response with list of all patients.
def plist(request):
    """
    return render(request, 'patients/list.html')
    """

    patients = Patient.objects.all
    return render(request, 'patients/index.html', {'tittle': 'Список','patients':patients})

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


# Get response with patient add menu.
def addUser(request):
    form = UserForm()
    if request.method == 'POST':
        print(request.POST)
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
    context = {'form': form}
    return render(request, 'patients/adduser.html', context)


def qrTest(request, uuid):
    args = {'uuid': uuid}
    return render(request, 'patients/qr.html', args)
