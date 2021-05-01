from django.contrib import admin
from . import models

@admin.register(models.FileModel)
class FileAdmin(admin.ModelAdmin):
    
    raw_id_fields = ("board",)

class FileInline(admin.TabularInline):
    model = models.FileModel

@admin.register(models.DocBoardModels)
class DocBoardAdmin(admin.ModelAdmin):

    inlines = (FileInline,)

    list_display = (
        "title",
        "author",
        "board_type",
        "created",
        "likeCount",

    )
    raw_id_fields = ("author",)