from django.contrib import admin
from . import models


class ContactFileinline(admin.TabularInline):
    model = models.ContactFileModel

@admin.register(models.ContactModel)
class  ContactModelAdmin(admin.ModelAdmin):

    inlines = (ContactFileinline,)