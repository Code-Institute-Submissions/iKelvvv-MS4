from django.shortcuts import render, get_object_or_404, reverse
from django.http import HttpResponseRedirect
# Import Django generic libary
from django.views import generic, View
from django.views.generic import TemplateView, DetailView
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
    queryset = Booking.objects.all()
    template_name = "manage_booking.html"
    paginate_by = 6

    def get_queryset(self): 
        return Booking.objects.filter(user_id=self.request.user)

class EditBooking(View):
    model = Booking
    queryset = Booking.objects.all()
    template_name = "edit_booking.html"
    context_object_name = 'edit_booking'

    def get(self, request, booking_id, *args, **kwargs):
        queryset = Booking.objects.all()
        booking = get_object_or_404(queryset, pk=booking_id)

        return render(
            request,
            "edit_booking.html",
            {
                "booking": booking
            })