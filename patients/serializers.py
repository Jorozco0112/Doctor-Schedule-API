from rest_framework import serializers

from patients.models import Patient, Insurance, MedicalRecord

class PatientSerializer(serializers.ModelSerializer):
    """This class serializes patient entity"""
    class Meta:
        model = Patient
        fields = '__all__'


class InsuranceSerializer(serializers.ModelSerializer):
    """This class serializes insurance entity"""
    class Meta:
        model = Insurance
        fields = '__all__'


class MedicalRecordSerializer(serializers.ModelSerializer):
    """This class serializes medical record entity"""
    class Meta:
        model = MedicalRecord
        fields = '__all__'
