from django.contrib import admin

from example_project.test_app.models import TestModel


@admin.register(TestModel)
class TestModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'eager_data', 'lazy_data']
    list_display_links = ['id', 'name']
