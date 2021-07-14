from rest_framework import serializers
from patients.models import Patient, Note


class PatientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Patient
        fields = '__all__'


class NoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Note
        fields = ('text', 'header', 'time_of_creation')