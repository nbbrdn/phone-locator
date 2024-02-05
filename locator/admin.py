from django.contrib import admin

from .models import DEFCode


@admin.register(DEFCode)
class DEFCodeAdmin(admin.ModelAdmin):
    list_display = ("id", "code", "start_range", "end_range", "operator", "region")
