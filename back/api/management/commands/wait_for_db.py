"""
Django command to wait for database.
"""
import time
import os
from psycopg2 import OperationalError as Psycopg2OpError
from django.db.utils import OperationalError
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    """Django command to wait for database."""

    def handle(self, *args, **options):
        """Entrypoint for command."""
        self.stdout.write("Waiting for database...")
        self.stdout.write(
            f"DB_USER: {os.environ.get('DB_USER')}, \
              DB_PASSWORD: {os.environ.get('DB_PASSWORD')}, \
              DB_NAME: {os.environ.get('DB_NAME')}, \
              DB_HOST: {os.environ.get('DB_HOST')}, \
              DB_PORT: {os.environ.get('DB_PORT')}"
        )
        db_up = False
        while db_up is False:
            try:
                self.check(databases=["default"])
                db_up = True
            except (Psycopg2OpError, OperationalError) as e:
                self.stdout.write(f"Database unavailable, waiting 1 second... {e}")
                time.sleep(1)

        self.stdout.write(self.style.SUCCESS("Database available!"))
