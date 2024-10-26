from django.urls import path
from patients.views import (
    PatientView,
    DetailPatientView,
    ListInsuranceView,
    DetailInsuranceView,
    ListMedicalRecordView,
    DetailMedicalRecordView,
)

urlpatterns = [
    path('patient', PatientView.as_view(), name='patient'),
    path('patient/<int:pk>/', DetailPatientView.as_view(), name='patient_detail'),
    path('insurances/', ListInsuranceView.as_view(), name='insurance'),
    path('insurances/<int:pk>/', DetailInsuranceView.as_view(), name='insurance-detail'),
    path('medicalrecords/', ListMedicalRecordView.as_view(), name='medical-record'),
    path(
        'medicalrecords/<int:pk>/',
        DetailMedicalRecordView.as_view(),
        name='medical-record-detail'
    ),
]
