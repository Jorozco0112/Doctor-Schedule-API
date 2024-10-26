from django.urls import path

from rest_framework.routers import DefaultRouter
from .views import (
    ListDepartmentView,
    DetailDepartmentView,
    ListDoctorAvailabilityView,
    DetailDoctorAvailabilityView,
    ListMedicalNoteView,
    DetailMedicalNoteView,
)
from .viewsets import DoctorViewSet

router = DefaultRouter()
router.register('doctors', DoctorViewSet)

urlpatterns = [
    path('departments/', ListDepartmentView.as_view()),
    path('departments/<int:id>/', DetailDepartmentView.as_view()),
    path('doctoravailabilities/', ListDoctorAvailabilityView.as_view()),
    path('doctoravailabilities/<int:id>/', DetailDoctorAvailabilityView.as_view()),
    path('medicalnotes/', ListMedicalNoteView.as_view()),
    path('medicalnotes/<int:id>/', DetailMedicalNoteView.as_view()),
] + router.urls
