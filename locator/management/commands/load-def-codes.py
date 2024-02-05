import csv

import requests
from django.core.management.base import BaseCommand

from locator.models import DEFCode


class Command(BaseCommand):

    def handle(self, *args, **options):
        url = "https://opendata.digital.gov.ru/downloads/ABC-3xx.csv"

        response = requests.get(url, verify=False)  # noqa: S501, S113

        if response.status_code == 200:
            csv_data = response.content.decode("utf-8").splitlines()
            csv_reader = csv.DictReader(csv_data, delimiter=";")

            DEFCode.objects.all().delete()

            for row in csv_reader:
                print(row)
                DEFCode.objects.create(
                    code=row["\ufeffАВС/ DEF"],
                    start_range=row["От"],
                    end_range=row["До"],
                    operator=row["Оператор"],
                    region=row["Регион"],
                )
