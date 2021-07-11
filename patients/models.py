import datetime
import uuid

from django.db import models


class Patient(models.Model):
    name = models.CharField(max_length=60)
    lastname = models.CharField(max_length=60)
    patronymic = models.CharField(max_length=60, null=True)
    date_of_birth = models.DateField()
    date_of_receipt = models.DateTimeField(default=datetime.datetime.now())
    diagnosis = models.CharField(max_length=100, null=True)
    appointment = models.TextField(max_length=10000, null=True)
    comment = models.TextField(max_length=10000, null=True)
    uuid = models.CharField(max_length=100, blank=True, unique=True, default=uuid.uuid4, primary_key=True)

    def __str__(self):
        return self.name + ' ' + self.lastname
