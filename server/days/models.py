from django.db import models
from django.utils import timezone
from shops.models import Shops

class Day(models.Model):
    shop = models.ForeignKey(Shops, related_name='days', on_delete=models.CASCADE)
    date = models.DateField(default=timezone.now)
    shirts_updated = models.IntegerField(default=0)
    pants_updated = models.IntegerField(default=0)
    safari_updated = models.IntegerField(default=0)
    each_day_total = models.FloatField(default=0.0)
    class Meta:
        unique_together = ('shop', 'date')  # One entry per shop per day

    def __str__(self):
        return f"{self.shop.name} - {self.date}"


class DayHistory(models.Model):
    shop = models.ForeignKey(Shops, related_name='day_histories', on_delete=models.CASCADE)
    date = models.DateField(default=timezone.now)
    shirts_updated = models.IntegerField(default=0)
    pants_updated = models.IntegerField(default=0)
    safari_updated = models.IntegerField(default=0)
    each_day_total = models.FloatField(default=0.0)

    class Meta:
        unique_together = ('shop', 'date')  # One entry per shop per day

    def __str__(self):
        return f"{self.shop.name} - {self.date} (History)"
