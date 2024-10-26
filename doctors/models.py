from django.db import models

# Create your models here.

class Doctor(models.Model):
    """
    This class maps doctor table
    """
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    qualification = models.CharField(max_length=100)
    contact_number = models.CharField(max_length=15)
    email = models.EmailField()
    address = models.TextField()
    biography = models.TextField()
    is_on_vacation = models.BooleanField(default=False)


class Department(models.Model):
    """
    This class maps department table
    """
    name = models.CharField(max_length=100)
    description = models.TextField()


class DoctorAvailability(models.Model):
    """This class maps doctor_availability table"""
    doctor = models.ForeignKey(
        Doctor,
        related_name='availabilities',
        on_delete=models.CASCADE
    )
    start_date = models.DateField()
    end_date = models.DateField()
    start_time = models.TimeField()
    end_time = models.TimeField()


class MedicalNote(models.Model):
    """This class maps medical_note table"""
    doctor = models.ForeignKey(
        Doctor, related_name='medical_notes', on_delete=models.CASCADE
    )
    note = models.TextField()
    date = models.DateField()
