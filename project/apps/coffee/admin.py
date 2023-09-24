from django.contrib import admin

from .models import Coffee, Feedback


class CoffeeAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'price', 'info')
    list_display_links = ('title', 'description', 'price', 'info')
    search_fields = ('title', 'description', 'price', 'info')


class FeedbackAdmin(admin.ModelAdmin):
    list_display = ('user', 'text', 'rating')
    list_display_links = ('user', 'rating')
    list_filter = ('rating',)


admin.site.register(Coffee, CoffeeAdmin)
admin.site.register(Feedback, FeedbackAdmin)
