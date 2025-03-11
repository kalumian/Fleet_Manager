from django.db import models
from .trip import Trip
from .driver import Driver
from ..Enums.log_status import LogStatus

class LogEntry(models.Model):
    trip = models.ForeignKey(Trip, on_delete=models.CASCADE, related_name='log_entries')
    driver = models.ForeignKey(Driver, on_delete=models.CASCADE)
    status = models.CharField(max_length=20, choices=LogStatus.CHOICES)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField(null=True, blank=True)
    location = models.CharField(max_length=255)

    # الساعات المسجلة بناءً على نوع النشاط
    total_driving_hours = models.FloatField(default=0)  # إجمالي ساعات القيادة
    total_off_duty_hours = models.FloatField(default=0)  # إجمالي ساعات الراحة
    total_sleeper_berth_hours = models.FloatField(default=0)  # إجمالي ساعات النوم
    total_on_duty_hours = models.FloatField(default=0)  # إجمالي ساعات العمل بدون القيادة
    total_miles_today = models.FloatField(default=0)  # إجمالي الأميال المقطوعة اليوم

    def __str__(self):
        return f"{self.driver.user.get_full_name()}: {self.get_status_display()} - {self.start_time.strftime('%Y-%m-%d %H:%M')}"
