from django.db import models

# Create your models here.
class Appointment(models.Model):
    reason = models.TextField()
    prescrciption = models.FileField(
        blank=True,
        upload_to='prescriptions/',
    )

    class Status(models.TextChoices):
        PENDING = 'PENDING', 'En attente'
        CONFIRMED = 'CONFIRMED', 'Confirmé'
        CANCELED = 'CANCELED', 'Annulé'
        status = models.CharField(choices=Status.choices, default=Status.PENDING, max_length=10)
        #status = models.CharField(choices=[(status, status.label) for status in Status], default=Status.PENDING, max_length=10)
        duration_minutes = models.PositiveIntegerField(default=30)
        created_at = models.DateTimeField(auto_now_add=True)
        updated_at = models.DateTimeField(auto_now=True)
        appointment_date = models.DateTimeField()
        Doctor = models.ForeignKey('AccountApp.Doctor', on_delete=models.CASCADE, related_name='appointments')
        Patient = models.ForeignKey('AccountApp.Patient', on_delete=models.CASCADE, related_name='appointments')
        