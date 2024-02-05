from django.db import models


class DEFCode(models.Model):
    code = models.IntegerField()
    start_range = models.IntegerField()
    end_range = models.IntegerField()
    operator = models.CharField(max_length=255)
    region = models.CharField(max_length=255)

    class Meta:
        indexes = (models.Index(fields=["code", "start_range", "end_range"]),)
