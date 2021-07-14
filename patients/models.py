import datetime
import uuid

import django
from django.db import models


class Patient(models.Model):
    name = models.CharField(max_length=60)
    lastname = models.CharField(max_length=60)
    patronymic = models.CharField(max_length=60, null=True)
    date_of_birth = models.DateField()
    date_of_receipt = models.DateTimeField(default=django.utils.timezone.now)
    diagnosis = models.CharField(max_length=100, null=True)
    appointment = models.TextField(max_length=10000, null=True)
    comment = models.TextField(max_length=10000, null=True)
    uuid = models.CharField(max_length=100, blank=True, unique=True, default=uuid.uuid4, primary_key=True)

    def __str__(self):
        return self.name + ' ' + self.lastname


class User(models.Model):
    login = models.CharField(max_length=60, unique=True)
    password_hash = models.CharField(max_length=200)
    token = models.CharField(max_length=100, blank=True, default=uuid.uuid4)

    def __str__(self):
        return self.login


class Note(models.Model):
    time_of_creation = models.DateTimeField(default=django.utils.timezone.now)
    header = models.CharField(max_length=60)
    text = models.TextField(max_length=10000)
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.time_of_creation) + ': ' + self.header


class Session(models.Model):
    auth_token = models.CharField(max_length=100, default=uuid.uuid4)
    login = models.CharField(max_length=60)
    last_used = models.DateTimeField(default=django.utils.timezone.now)
