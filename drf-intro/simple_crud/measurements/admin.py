from django.contrib import admin
from django.core.exceptions import ValidationError

from measurements.models import Project, Measurement


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('id','name', 'latitude', 'longitude')
    list_display_links = ('id','name')

@admin.register(Measurement)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('id','value', 'project')
    list_display_links = ('id','value')

