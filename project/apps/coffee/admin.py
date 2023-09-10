from django.contrib import admin
from .models import Coffee, Feedback

admin.site.register(Coffee)


@admin.register(Feedback)
class FeedbackAdmin(admin.ModelAdmin):
    list_display = ['user', 'text', 'rating']
