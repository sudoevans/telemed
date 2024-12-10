from africastalking import initialize, SMS
from django.db.models.signals import post_save
from django.dispatch import receiver
from appointments.models import Appointment
from .models import Notification
from rest_framework import viewsets, permissions
from .serializers import NotificationSerializer
from django.conf import settings


# LOAD APIS FROM ENV
AFRICASTALKING_API_KEY=settings.AFRICASTALKING_API_KEY
AFRICASTALKING_USERNAME=settings.AFRICASTALKING_USERNAME

@receiver(post_save, sender=Appointment)
def create_appointment_notification(sender, instance, created, **kwargs):
    if created:
        Notification.objects.create(
            user=instance.user,
            title="New Appointment Scheduled",
            message=f"You have an appointment on {instance.date}.",
            notification_type="appointment",
        )       

def send_notification(notification):
    if notification.notification_type == 'email':
         pass
    elif notification.notification_type == 'sms':
        initialize(AFRICASTALKING_USERNAME, AFRICASTALKING_API_KEY)
        sms = SMS
        response = sms.send(notification.message, [notification.user.phone_number])
        print(response)  # Optional: Log the response for debugging
    notification.sent = True
    notification.save()


class NotificationViewSet(viewsets.ModelViewSet):
    serializer_class = NotificationSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Notification.objects.filter(user=self.request.user)
