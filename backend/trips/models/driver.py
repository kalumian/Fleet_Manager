from django.db import models
from django.contrib.auth.models import User

class Driver(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    license_number = models.CharField(max_length=50)
    phone_number = models.CharField(max_length=15)


    available_hours = models.FloatField(default=70)  # الحد الأقصى المسموح به خلال 8 أيام
    hours_used_last_8_days = models.FloatField(default=0)  # الساعات المستهلكة في آخر 8 أيام
    hours_remaining_today = models.FloatField(default=11)  # الحد الأقصى للقيادة في اليوم

    route = models.JSONField(default=dict, blank=True, null=True)

    def __str__(self):
        return f"{self.user.get_full_name()} - {self.license_number}"
