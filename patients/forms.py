from datetime import datetime

from django import forms
from django.forms import ModelForm
from .models import Patient


class PatientForm(ModelForm):
    class Meta:
        model = Patient
        fields = '__all__'
        exclude = ('uuid',)
        labels = {
            'name': 'Имя',
            'lastname': 'Фамилия',
            'patronymic': 'Отчество*',
            'date_of_birth': 'Дата рождения*',
            'date_of_receipt': 'Дата и время поступления',
            'diagnosis': 'Диагноз*',
            'appointment': 'Назначение*',
            'comment': 'Комментарий',
        }
        widgets = {
            'date_of_birth': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'date_of_receipt': forms.DateTimeInput(attrs={'class': 'form-control', 'type': 'datetime'}),
        }
