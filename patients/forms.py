import hashlib
from datetime import datetime

from django import forms
from django.forms import ModelForm,TextInput,Textarea
from .models import Patient, User


class UploadFileForm(forms.Form):
    title = forms.CharField(max_length=50)
    file = forms.FileField()

class PatientForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super(PatientForm, self).__init__(*args, **kwargs)

    class Meta:
        model = Patient
        fields = '__all__'
        exclude = ('uuid',)
        labels = {
            'name': 'Имя',
            'lastname': 'Фамилия',
            'patronymic': 'Отчество*',
            'date_of_birth': 'Дата рождения*',
            'date_of_receipt': 'Дата и время поступления*',
            'diagnosis': 'Диагноз*',
            'appointment': 'Назначение*',
            'comment': 'Комментарий*',
            'picture': 'Фото',
        }
        widgets = {
            "name": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Введите имя'
            }),

            "lastname": Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Введите фамилию'
            }),

            'date_of_birth': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'date_of_receipt': forms.DateTimeInput(attrs={'class': 'form-control', 'type': 'datetime'}),
            'picture': forms.FileInput()
        }


class UserForm(ModelForm):
    password = forms.CharField(label='Пароль')

    class Meta:
        model = User
        fields = '__all__'
        exclude = ('token', 'password_hash')
        labels = {
            'login': "Логин",
        }

    def save(self, commit=True):
        super(UserForm, self).save(commit=commit)
        return User.objects.filter(login=self.cleaned_data['login']).update(login=self.cleaned_data['login'], password_hash=hashlib.sha256(self.cleaned_data['password'].encode('utf-8')).hexdigest())

