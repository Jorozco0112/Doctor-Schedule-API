from django.urls import path
from patients.views import PatientView, DetailPatientView

urlpatterns = [
    path('patient', PatientView.as_view(), name='patient'),
    path('patient/<int:pk>/', DetailPatientView.as_view(), name='patient_detail')
]
