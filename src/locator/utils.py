from .models import DEFCode
import requests
import csv


def fetch_def_codes():
    urls = [
        "https://opendata.digital.gov.ru/downloads/ABC-3xx.csv",
        "https://opendata.digital.gov.ru/downloads/ABC-4xx.csv",
        "https://opendata.digital.gov.ru/downloads/ABC-8xx.csv",
        "https://opendata.digital.gov.ru/downloads/DEF-9xx.csv",
    ]

    DEFCode.objects.all().delete()

    for url in urls:
        csv_data = fetch_csv_data(url)

        if csv_data:
            def_codes = parse_csv_data(csv_data)
            DEFCode.objects.bulk_create(def_codes)


def fetch_csv_data(url):
    response = requests.get(url, verify=False)  # noqa: S501, S113
    if response.status_code == 200:
        return response.content.decode("utf-8").splitlines()
    return None


def parse_csv_data(csv_data):
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

    return def_codes
