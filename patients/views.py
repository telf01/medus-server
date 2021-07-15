import datetime
import hashlib
import uuid

import django
from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.http import HttpResponseNotFound
from .forms import PatientForm, UserForm, UploadFileForm
from .models import Patient, Session, User



# Get response with list of all patients.
def plist(request):
    if checkCookies(request):
        """
        return render(request, 'patients/list.html')
        """

        patients = Patient.objects.all
        return render(request, 'patients/index.html', {'tittle': 'Список','patients':patients})
    else:
        return redirect('/login')

def checkCookies(request):
    if 'auth_token' in request.COOKIES:
        t = Session.objects.filter(auth_token=request.COOKIES['auth_token']).last()
        if datetime.datetime.now().hour - t.last_used.hour > 144:
            t.delete()
            return False
        else:
            t.last_used = datetime.datetime.now()
            return True

# Get response with patient add menu.
def add(request):
    if checkCookies(request):
        form = PatientForm()
        if request.method == 'POST':
            print(request.POST)
            form = PatientForm(request.POST, request.FILES)
            print(form.is_valid())
            if form.is_valid():

                form.save()

                return redirect('/')
        context = {'form': form}
        return render(request, 'patients/add.html', context)
    else:
        return redirect('/login')

def upload_file(request):
    if request.method == 'POST':
        data = request.POST
        print(request.FILES['picture'])
        return HttpResponseRedirect('/success/url/')
    else:
        form = UploadFileForm()
    return render(request, 'patients/upload.html')

def login(request):
    if request.method == 'POST':
        if User.objects.filter(login=request.POST['login']).exists():
            user = User.objects.filter(login=request.POST['login']).first()
        else:
            return HttpResponse('Net')

        if hashlib.sha256(str(request.POST['password']).encode('UTF-8')).hexdigest() == user.password_hash:
            if Session.objects.filter(login=user).exists():
                response = HttpResponseRedirect('/')
                response.set_cookie('auth_token', Session.objects.filter(login=user).first().auth_token)
                return response
            else:
                t = uuid.uuid4()
                Session.objects.create(login=user.login, last_used=datetime.datetime.now(), auth_token=t)
                response = HttpResponseRedirect('/')
                response.set_cookie('auth_token', t)
                return response

    return render(request, 'patients/login.html')


# Get response with patient add menu.
def addUser(request):
    if checkCookies(request):
        form = UserForm()
        if request.method == 'POST':
            print(request.POST)
            form = UserForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect('/')
        context = {'form': form}
        return render(request, 'patients/adduser.html', context)
    else:
        return redirect('/login')


def qrTest(request, uuid):
    args = {'uuid': uuid}
    return render(request, 'patients/qr.html', args)


def edit(request, uuid):

    try:

        patients = Patient.objects.get(uuid=uuid)

        if request.method == "POST":
            print(request.POST)
            patients.name = request.POST.get("name")
            patients.lastname = request.POST.get("lastname")
            patients.patronymic = request.POST.get("patronymic")
            patients.date_of_birth = request.POST.get("date_of_birth")
            patients.date_of_receipt = request.POST.get("date_of_receipt")
            patients.diagnosis = request.POST.get("diagnosis")
            patients.appointment = request.POST.get("appointment")
            patients.comment = request.POST.get("comment")
            patients.save()

            return HttpResponseRedirect("/")
        else:
            return render(request, "patients/edit.html", {"patients": patients})
    except Patient.DoesNotExist:
        return HttpResponseNotFound("<h2>Person not found</h2>")


def delete(request, uuid):
    try:
        patients = Patient.objects.get(uuid=uuid)
        patients.delete()
        return HttpResponseRedirect("/")
    except Patient.DoesNotExist:
        return HttpResponseNotFound("<h2>Person not found</h2>")
