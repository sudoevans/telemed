# doctors/views.py
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
from rest_framework.exceptions import PermissionDenied
from .models import Doctor
from .serializers import DoctorSerializer

class DoctorViewSet(ModelViewSet):
    queryset = Doctor.objects.all()
    serializer_class = DoctorSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        if not self.request.user.is_staff:  # Assuming 'is_doctor' field exists
            raise PermissionDenied("Only staff can create doctor profiles.")
        serializer.save(user=self.request.user)
