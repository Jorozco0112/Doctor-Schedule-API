from rest_framework import serializers

from bookings.models import Appointment, MedicalNote


class AppointmentSerializer(serializers.ModelSerializer):
    """This class serializes appointment entity"""

    class Meta:
        model = Appointment
        fields = '__all__'


class MedicalNoteSerializer(serializers.ModelSerializer):
    """This class serializes appointment entity"""

    class Meta:
        model = MedicalNote
        fields = '__all__'
