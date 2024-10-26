from django.urls import reverse
from django.test import TestCase

from rest_framework import status
from rest_framework.test import APIClient

from patients.models import Patient
from doctors.models import Doctor
from doctors.viewsets import DoctorViewSet

# Create your tests here.

class DoctorViewSetTests(TestCase):

    def setUp(self):
        self.patient = Patient.objects.create(
            first_name='Luis',
            last_name='Martinez',
            date_of_birth='1990-12-05',
            contact_number='3224452456',
            email='example@example.com',
            address='Direccion de prueba',
            medical_history='Ninguna'
        )
        self.doctor = Doctor.objects.create(
            first_name='Javier',
            last_name='Orozco',
            qualification='Profesional',
            contact_number='234531134',
            email='example2@example.com',
            address='Barranquilla',
            biography='Sin',
            is_on_vacation=False
        )
        self.client = APIClient()

    def test_list_should_return_200(self):
        """This test expect a 200 status code"""
        url = reverse(
            'doctor-appointment',
            kwargs={"pk": self.doctor.id}
        )
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
