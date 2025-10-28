from django.core.management.base import BaseCommand
from mailing.models import Mailing
from datetime import datetime


class Command(BaseCommand):
    help = 'Send scheduled mailings'

    def handle(self, *args, **options):
        # Логика отправки рассылок
        mailings = Mailing.objects.filter(status='started')
        self.stdout.write(f"Sending {mailings.count()} mailings")
