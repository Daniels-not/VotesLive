from django.contrib import admin

from .models import *

admin.site.site_header = "Vote Live"
admin.site.site_title = "Vote live admin area"
admin.site.index = "Welcome to Vote live admin area"


# Register your models here.

class ChoiceInline(admin.TabularInline):
    model = Choices
    extra = 3


class QuestionsAdmin(admin.ModelAdmin):
    fieldsets = [(None, {"fields": ["question_text"]}),
                 ("Data Information", {"fields": ["publication_date"], "classes": ["collapse"]}) ]
    inlines = [ChoiceInline]


admin.site.register(Questions, QuestionsAdmin)
