# serializers.py
from datetime import timezone
from rest_framework import serializers
from .models import Appointment

class AppointmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Appointment
        fields = ['id', 'patient', 'doctor', 'appointment_time', 'status', 'notes']
        read_only_fields = ['patient', 'status']

    def validate_appointment_time(self, value):
        if value < timezone.now():
            raise serializers.ValidationError("Appointment time cannot be in the past.")
        return value
    def validate(self, attrs):
        # Check for double booking
        if Appointment.objects.filter(doctor=attrs['doctor'], appointment_time=attrs['appointment_time']).exists():
            raise serializers.ValidationError("This doctor already has an appointment scheduled for this time.")
        return attrs