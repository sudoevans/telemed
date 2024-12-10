from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from .models import Appointment
from notifications.models import Notification  # Assuming notifications app exists


@receiver(post_save, sender=Appointment)
def send_appointment_notification(sender, instance, created, **kwargs):
    """Trigger notifications when an appointment is created or updated."""
    if created:
        # Notify the patient and doctor about the new appointment
        Notification.objects.create(
            user=instance.patient,
            title="Appointment Scheduled",
            message=f"Your appointment with Dr. {instance.doctor.first_name} is scheduled for {instance.appointment_time}.",
            notification_type="appointment",
        )
        Notification.objects.create(
            user=instance.doctor,
            title="New Appointment Scheduled",
            message=f"An appointment with {instance.patient.first_name} is scheduled for {instance.appointment_time}.",
            notification_type="appointment",
        )
    else:
        # Notify about status changes
        Notification.objects.create(
            user=instance.patient,
            title="Appointment Updated",
            message=f"Your appointment status with Dr. {instance.doctor.first_name} on {instance.appointment_time} has changed to {instance.status}.",
            notification_type="appointment",
        )


@receiver(post_delete, sender=Appointment)
def send_appointment_deletion_notification(sender, instance, **kwargs):
    """Trigger notifications when an appointment is deleted."""
    Notification.objects.create(
        user=instance.patient,
        title="Appointment Canceled",
        message=f"Your appointment with Dr. {instance.doctor.first_name} scheduled for {instance.appointment_time} has been canceled.",
        notification_type="appointment",
    )
    Notification.objects.create(
        user=instance.doctor,
        title="Appointment Canceled",
        message=f"An appointment with {instance.patient.first_name} scheduled for {instance.appointment_time} has been canceled.",
        notification_type="appointment",
    )
