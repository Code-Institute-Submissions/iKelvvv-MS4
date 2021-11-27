from django.shortcuts import render
# Import Django generic libary
from django.views import generic
# Import Booking model from models
from .models import Booking

# Create your views here.
class BookingList(generic.ListView):
    model = Booking
    template_name = "index.html"
    paginate_by = 6
