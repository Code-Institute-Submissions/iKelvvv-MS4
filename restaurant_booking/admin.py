from django.contrib import admin
# Import Booking model from models.py
from .models import Booking

# Register your models here.
# admin.site.register(Booking)
# list_filter = ('status', 'booking_time', 'booking_date')


@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    list_filter = ('status', 'booking_time', 'booking_date')
    readonly_fields = ('title',)
    list_display = ('title', 'user_id', 'booking_date', 'booking_time', 'guest_count')
    search_fields = ('title', 'user_id')
    actions = ['approve_booking']

    def approve_booking(self, request, queryset):
        queryset.update(approve_booking=True)