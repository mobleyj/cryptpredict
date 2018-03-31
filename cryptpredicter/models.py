from django.db import models

# Create your models here.


class BpiPriceUpdate(models.Model):
    update_time = models.DateTimeField(),
    usd_value = models.FloatField(),
    gbp_value = models.FloatField(),
    eur_value = models.FloatField()
