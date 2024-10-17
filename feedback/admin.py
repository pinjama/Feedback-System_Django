from django.contrib import admin
from .models import Topic, Feedback
from import_export import resources
from import_export.admin import ImportExportModelAdmin

class TopicAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ['name']

class FeedbackResource(resources.ModelResource):

    class Meta:
        model = Feedback

class FeedbackAdmin(ImportExportModelAdmin):
    resource_classes = [FeedbackResource]
    list_display = ('aihe', 'arvosana', 'ruusut', 'risut', 'ideat', 'nimi', 'date')
    list_filter = ['aihe', 'date']
    search_fields = ['ruusut', 'risut', 'ideat']

admin.site.register(Topic, TopicAdmin)
admin.site.register(Feedback, FeedbackAdmin)