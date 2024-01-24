from celery import shared_task

from .utils import fetch_def_codes


@shared_task
def proc_fetch_def_codes():
    fetch_def_codes()
