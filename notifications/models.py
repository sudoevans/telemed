from django.db import models
from django.conf import settings

# Nofication Model: Creating this just incase we may need to extend it in future
class Notification(models.Model):
    CHOICE_NOTIFICATION_TYPE=[
        ('general', 'General'),
        ('appointment', 'Appointment'),
    ]
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='notifications')
    title = models.CharField(max_length=255)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    is_read = models.BooleanField(default=False)

    # For extensibility: Type of notification (e.g., appointment, general)
    notification_type = models.CharField(max_length=50, choices=CHOICE_NOTIFICATION_TYPE, blank=True, null=True, default='general')

    def __str__(self):
        return f"{self.user.email} - {self.title}"
