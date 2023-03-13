from django.contrib import admin

from . import models


@admin.register(models.Tutorial)
class TutorialAdmin(admin.ModelAdmin):
    list_display = ["title", "description", "date_added", "url", "owner"]
    search_fields = ["title", "description"]
    list_filter = ["date_added", "owner"]
