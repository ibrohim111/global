from django.contrib import admin
from apk.models import GlobalData

@admin.register(GlobalData)
class GlobalDataAdmin(admin.ModelAdmin):
    list_display = ["id", "file", "text", "number", "created_at"]
    list_display_links = ["id",]
