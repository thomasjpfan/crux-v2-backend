from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.admin import register, ModelAdmin

from .models import Dataset
from .models import DatasetTag
from .models import User
from .models import Analysis
from .models import AnalysisTag
from .models import Task


@register(Dataset)
class DatasetAdmin(ModelAdmin):
    list_display_links = ('name', )
    list_display = ('name', 'created_by')


@register(DatasetTag)
class DatasetTagAdmin(ModelAdmin):
    list_display_links = ('name', )
    list_display = ('name', )


@register(Analysis)
class AnalysisAdmin(ModelAdmin):
    list_display_links = ('id', 'name', 'dataset')
    list_display = ('id', 'name', 'dataset', 'created_by')


@register(AnalysisTag)
class AnalysisTagAdmin(ModelAdmin):
    list_display_links = ('name', )
    list_display = ('name', )


@register(Task)
class TaskAdmin(ModelAdmin):
    list_display_links = ('id', 'name')
    list_display = ('id', 'name', 'created_by')


# Register your models here.
admin.site.register(User, UserAdmin)
