from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework.generics import (
    ListCreateAPIView,
    RetrieveUpdateDestroyAPIView
)
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from drf_spectacular.utils import extend_schema

from patients.serializers import (
    PatientSerializer,
    InsuranceSerializer,
    MedicalRecordSerializer
)
from patients.models import Patient, Insurance, MedicalRecord

class PatientView(APIView):
    """
    Lists all patients or creates a new patient, depending on the HTTP method.
    """
    allowed_methods = ['GET', 'POST']
    permission_classes = (IsAuthenticated,)

    @extend_schema(
        responses={
            status.HTTP_200_OK:PatientSerializer
        }
    )
    def get(self, request):
        """
        Lists all patients.
        """
        patients = Patient.objects.all()
        serializer = PatientSerializer(patients, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        """Creates a new patient"""
        serializer = PatientSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(
                {
                    'message': "Patient saved successfully",
                    'patient': serializer.data
                },
                status=status.HTTP_201_CREATED
            )
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class DetailPatientView(APIView):
    """
    Retrieves, updates, or deletes a specific patient by ID, depending on the HTTP method.
    """
    allowed_methods = ['GET', 'PUT', 'DELETE']
    permission_classes = (IsAuthenticated,)

    def get_patient(self, pk):
        """This function retrieve the patient object
        by a given pk"""
        return get_object_or_404(Patient, pk=pk)

    def get(self, request, pk):
        "This service retrieve patient detail"
        patient = self.get_patient(pk=pk)
        serializer = PatientSerializer(patient)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, pk):
        "This function update a specific patient by ID"
        patient = self.get_patient(pk=pk)
        serializer = PatientSerializer(patient, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(
                {'message': 'Patient updated successfully', 'patient': serializer.data},
                status=status.HTTP_200_OK
            )
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        "This service delete a specific patient by ID"
        patient = self.get_patient(pk=pk)
        patient.delete()
        return Response(
            {'message': 'Patient deleted successfully'},
            status=status.HTTP_204_NO_CONTENT
        )


class ListInsuranceView(ListCreateAPIView):
    """This class handles POST and GET
    method from Insurance entity"""
    allowed_methods = ['GET', 'POST']
    serializer_class = InsuranceSerializer
    queryset = Insurance.objects.all()


class DetailInsuranceView(RetrieveUpdateDestroyAPIView):
    """This class handle GET, PUT and DELETE
    method from Insurance entity
    """
    allowed_methods = ['GET', 'PUT', 'DELETE']
    serializer_class = InsuranceSerializer
    queryset = Insurance.objects.all()


class ListMedicalRecordView(ListCreateAPIView):
    """This class handles POST and GET
    method from MedicalRecord entity"""
    allowed_methods = ['GET', 'POST']
    serializer_class = MedicalRecordSerializer
    queryset = MedicalRecord.objects.all()


class DetailMedicalRecordView(RetrieveUpdateDestroyAPIView):
    """This class handle GET, PUT and DELETE
    method from Medical Record entity
    """
    allowed_methods = ['GET', 'PUT', 'DELETE']
    serializer_class = MedicalRecordSerializer
    queryset = MedicalRecord.objects.all()
