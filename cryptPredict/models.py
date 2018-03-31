from django.db import models


class BpiPriceIndex:
    update_time = models.DateTimeField()
    usd_value = models.FloatField()
    gpb_value = models.FloatField()
    eur_value = models.FloatField()