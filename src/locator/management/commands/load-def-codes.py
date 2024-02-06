import csv

import requests
from django.core.management.base import BaseCommand

from locator.models import DEFCode


class Command(BaseCommand):

    def handle(self, *args, **options):
        urls = [
            "https://opendata.digital.gov.ru/downloads/ABC-3xx.csv",
            "https://opendata.digital.gov.ru/downloads/ABC-4xx.csv",
            "https://opendata.digital.gov.ru/downloads/ABC-8xx.csv",
            "https://opendata.digital.gov.ru/downloads/DEF-9xx.csv",
        ]

        DEFCode.objects.all().delete()

        for url in urls:
            response = requests.get(url, verify=False)  # noqa: S501, S113

            if response.status_code == 200:
                csv_data = response.content.decode("utf-8").splitlines()
                csv_reader = csv.DictReader(csv_data, delimiter=";")

                def_codes = []

                for row in csv_reader:
                    def_code = DEFCode(
                        code=row["\ufeffАВС/ DEF"],
                        start_range=row["От"],
                        end_range=row["До"],
                        operator=row["Оператор"],
                        region=row["Регион"],
                    )
                    def_codes.append(def_code)

                DEFCode.objects.bulk_create(def_codes)
