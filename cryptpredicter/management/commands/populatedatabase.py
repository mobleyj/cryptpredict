import requests
from django.core.management.base import BaseCommand, CommandError

from cryptpredicter.models import BpiPriceUpdate


def populate_database():
    url = 'https://api.coindesk.com/v1/bpi/historical/close.json'

    response = requests.get(url)
    data = response.json()
    i = 0
    for k, v in data['bpi'].items():
        row = BpiPriceUpdate.objects.get_or_create(update_time=k, usd_value=v)
        row.save()
        i += 1
    yield (i)


class Command(BaseCommand):

    def handle(self, *args, **options):
        for i in populate_database():
            print(i + ' rows created')