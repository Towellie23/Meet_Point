from django.contrib import admin
from .models import Event, Participation


@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_display = ('title', 'date', 'location', 'organizer')
    search_fields = ('title', 'description')
    list_filter = ('date', 'organizer')


@admin.register(Participation)
class ParticipationAdmin(admin.ModelAdmin):
    list_display = ('user', 'event', 'status')
    list_filter = ('status',)

