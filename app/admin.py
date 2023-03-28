from django.contrib import admin
from .models import Article
# Register your models here.
from import_export.admin import ImportExportModelAdmin
@admin.register(Article)
class userdata(ImportExportModelAdmin):
    pass