from django_filters import rest_framework as filters
from .models import Appointment

class AppointmentFilter(filters.FilterSet):
    date_range = filters.DateFromToRangeFilter(field_name='appointment_time')

    class Meta:
        model = Appointment
        fields = ['status', 'doctor', 'patient', 'date_range']
