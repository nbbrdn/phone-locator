from django.core.management.base import BaseCommand
from django_celery_beat.models import PeriodicTask, IntervalSchedule


class Command(BaseCommand):
    def handle(self, *args, **options):
        interval, _ = IntervalSchedule.objects.get_or_create(
            every=1, period=IntervalSchedule.DAYS
        )

        PeriodicTask.objects.create(
            interval=interval,
            name="fetch-def-codes",
            task="locator.tasks.proc_fetch_def_codes",
        )

        print("Task scheduled!")
