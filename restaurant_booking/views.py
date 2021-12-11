from django.shortcuts import render
# Import Django generic libary
from django.views import generic
# Import Booking model from models
from .models import Booking


# Create your views here.
class HomeView(generic.ListView):
    model = Booking
    template_name = "index.html"


class MenuView(generic.ListView):
    model = Booking
    template_name = "menu.html"


class ContactView(generic.ListView):
    model = Booking
    template_name = "contact.html"


class OnlineBookingView(generic.ListView):
    model = Booking
    template_name = "online_booking.html"


class EditProfile(generic.ListView):
    model = Booking
    template_name = "edit_profile.html"


class ManageBooking(generic.ListView):
    model = Booking
    template_name = "manage_booking.html"

