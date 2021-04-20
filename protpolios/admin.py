from django.contrib import admin
from . import models

@admin.register(models.ProtPolioModel)
class ProtPolioAdmin(admin.ModelAdmin):

    list_display = (
        "title",
        "url",
    )

    filter_horizontal = ("participants",)