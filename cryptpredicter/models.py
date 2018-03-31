
from django.db import models

# Create your models here.
from django.utils import timezone


class BpiPriceUpdate(models.Model):
    update_time = models.DateTimeField(default=timezone.now)
    usd_value = models.FloatField(default=0.0)
    gbp_value = models.FloatField(null=True, default=0.0)
    eur_value = models.FloatField(null=True, default=0.0)


class FuturePrediction(models.Model):
    prediction_time = models.DateTimeField(default=timezone.now)
    usd_prediction = models.FloatField(default=0.0)
    gpb_value = models.FloatField(default=0.0)
    eur_value = models.FloatField(default=0.0)