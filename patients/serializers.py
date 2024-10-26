from datetime import date
from rest_framework import serializers

from patients.models import Patient, Insurance, MedicalRecord
from bookings.serializers import AppointmentSerializer

class PatientSerializer(serializers.ModelSerializer):
    """This class serializes patient entity"""
    appointments = AppointmentSerializer(many=True, read_only=True)
    age = serializers.SerializerMethodField()
    class Meta:
        model = Patient
        fields = (
            'id',
            'first_name',
            'last_name' ,
            'age',
            'date_of_birth', 
            'email',
            'address',
            'medical_history',
            'appointments',
        )

    def get_age(self, obj:Patient):
        """This method return the age
        of Patient instance"""
        age_td = date.today() - obj.date_of_birth
        return age_td.days // 365


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
