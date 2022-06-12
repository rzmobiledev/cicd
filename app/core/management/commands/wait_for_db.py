"""
Django command to wait for database ready
"""
from django.core.management.base import BaseCommand
import time
from psycopg2 import OperationalError as Psycopg2Error
from django.db.utils import OperationalError


class Command(BaseCommand):
    """Django command to wait for database."""
    def handle(self, *args, **options):
        """Entry point for command."""
        self.stdout.write('Waiting for database...')
        wakeup_db = False

        while wakeup_db is False:
            try:
                self.check(databases=['default'])
                wakeup_db = True

            except(Psycopg2Error, OperationalError):
                self.stdout.write('Waiting for 2 second...')
                time.sleep(2)
        self.stdout.write(self.style.SUCCESS('YOUR DATABASE IS READY!'))
