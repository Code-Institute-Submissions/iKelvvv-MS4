from .models import Booking
from django import forms


class UpdateBookingDetails(forms.ModelForm):
    class Meta:
        model = Booking
        fields = ('booking_date', 'booking_time', 'booking_comments', 'guest_count',)