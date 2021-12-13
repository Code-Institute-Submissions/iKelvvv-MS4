from django.shortcuts import render
# Import Django generic libary
from django.views import generic, View
from django.views.generic import TemplateView
# Import Booking model from models
from .models import Booking


# Create your views here.
class HomeView(TemplateView):
    template_name = "index.html"


class MenuView(TemplateView):
    template_name = "menu.html"


class ContactView(TemplateView):
    template_name = "contact.html"


class OnlineBookingView(TemplateView):
    template_name = "online_booking.html"


class EditProfile(TemplateView):
    template_name = "edit_profile.html"


class ManageBooking(generic.ListView): 
    model = Booking
    template_name = "manage_booking.html"
    paginate_by = 6

    def get_booking_data(request):
        bookings = Booking.objects.all()
        context = {
            'bookings': bookings
        }
        return render(request, 'manage_booking/', context)
        
