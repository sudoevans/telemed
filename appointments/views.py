# views.py
from rest_framework import generics, permissions
from .models import Appointment
from .serializers import AppointmentSerializer

class AppointmentListCreateView(generics.ListCreateAPIView):
    queryset = Appointment.objects.all()
    serializer_class = AppointmentSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(patient=self.request.user)  # Automatically set the patient to the logged-in user

class AppointmentDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Appointment.objects.all()
    serializer_class = AppointmentSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        # Allow users to see only their own appointments
        return self.queryset.filter(patient=self.request.user)
    def perform_update(self, serializer):
        # Allow rescheduling only if the appointment is still scheduled
        appointment = self.get_object()
        if appointment.status != 'scheduled':
            raise serializers.ValidationError("Cannot reschedule a completed or canceled appointment.")
        serializer.save()

    def perform_destroy(self, instance):
        # Update the status to canceled instead of deleting the appointment
        instance.status = 'canceled'