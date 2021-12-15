from django.contrib import admin
# Import Booking model from models.py
from .models import Booking

# Register your models here.
# admin.site.register(Booking)
# list_filter = ('status', 'booking_time', 'booking_date')


@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    list_filter = ('status', 'booking_time', 'booking_date')
    readonly_fields = ('booking_id',)
    list_display = ('booking_id', 'user_id', 'booking_date', 'booking_time', 'guest_count', 'status', 'created_on')
    search_fields = ('booking_id', 'user_id')
    actions = ['approve_booking']

    def approve_booking(self, request, queryset):
        queryset.update(approve_booking=True)