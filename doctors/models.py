from django.db import models
from users.models import User
from phonenumber_field.modelfields import PhoneNumberField

# Create your models here.
class Doctor(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    specialization = models.CharField(max_length=100)
    license_number = models.CharField(max_length=50)
    contact_number = PhoneNumberField()