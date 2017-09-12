from django.contrib import admin
from .models import School


# Register your models here.
class SchoolAdmin(admin.ModelAdmin):
    school_display = ('name')
    search_fields = ['name']

admin.site.register(School, SchoolAdmin)