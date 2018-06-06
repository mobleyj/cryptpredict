from django.core.management.base import BaseCommand

from cryptpredicter.cron import populate_database


class Command(BaseCommand):

    def handle(self, *args, **options):
        for i in populate_database():
            print(str(i) + ' rows created')
