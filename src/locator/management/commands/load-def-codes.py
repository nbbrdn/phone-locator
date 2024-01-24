import csv

import requests
from django.core.management.base import BaseCommand

from locator.models import DEFCode

from locator.utils import fetch_def_codes


class Command(BaseCommand):

    def handle(self, *args, **options):
        fetch_def_codes()
