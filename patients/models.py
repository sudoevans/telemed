# Create your models here.
from django.db import models
from users.models import User
from phonenumber_field.modelfields import PhoneNumberField


class Patient(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    medical_record_number = models.CharField(max_length=50, unique=True)
    date_of_birth = models.DateField(null=True, blank=True)
    contact_number =PhoneNumberField(null=True, blank=True)


    def __str__(self):
        return f"{self.user.email} - Patient"
