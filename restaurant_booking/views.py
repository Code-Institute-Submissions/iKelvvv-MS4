from django.shortcuts import render, get_object_or_404, reverse
from django.http import HttpResponseRedirect
# Import Django generic libary
from django.views import generic, View
from django.views.generic import TemplateView, DetailView, UpdateView, DeleteView
# Import Booking model from models
from .models import Booking, UserProfile
from .forms import UpdateBookingDetails, EditProfileForm
from django.shortcuts import redirect

# Create your views here.
class HomeView(TemplateView):
    template_name = "index.html"


class MenuView(TemplateView):
    template_name = "menu.html"


class ContactView(TemplateView):
    template_name = "contact.html"


class CreateProfile(View):
    template_name = "create_profile.html"
    
    def get(self, request, *args, **kwargs):
        return render(
            request,
            "create_profile.html",
        )

    def post(self, request):
        f_name = request.POST.get("f_name")
        l_name = request.POST.get("l_name")
        tele = request.POST.get("phone_number")

        CreateUserProfile = UserProfile.objects.create(
            first_name=f_name,
            last_name=l_name,
            phone_number=tele,
            user=request.user,
        )

        CreateUserProfile.save()

        return redirect(reverse('home'))


class EditProfile(UpdateView):
    template_name = "edit_profile.html"

    def get(self, request, *args, **kwargs):
        form = EditProfileForm

        return render(
            request,
            "edit_profile.html",
            {
                "form": form,
                "updated": False,
            }
        )

    def post(self, request, *args, **kwargs):
        users_profile = UserProfile.user

        update_profile = EditProfileForm(request.POST, instance=users_profile)

        if update_profile.is_valid():
            profile_updates = update_profile.save()
        else:
            update_profile = EditProfileForm(instance=users_profile)

        return render(
            request,
            "edit_profile.html",
            {
                "form": form,
                "updated": False,
            },
        )


class ManageBooking(generic.ListView): 
    model = Booking
    queryset = Booking.objects.all()
    template_name = "manage_booking.html"
    paginate_by = 6

    def get_queryset(self): 
        return Booking.objects.filter(user_id=self.request.user)


class OnlineBookingView(View):
    template_name = "online_booking.html"

    def get(self, request, *args, **kwargs):
        return render(
            request,
            "online_booking.html",
        )

    def post(self, request):
        date = request.POST.get("date")
        time = request.POST.get("time")
        guest_count = request.POST.get("guest_count")
        comments = request.POST.get("comments")

        online_booking = Booking.objects.create(
            booking_date=date,
            booking_time=time,
            guest_count=guest_count,
            user=request.user,
            booking_comments=comments
        )

        online_booking.save()

        return redirect(reverse('manage_booking'))


class EditBooking(View):
    model = Booking
    # queryset = Booking.objects.all()
    template_name = "edit_booking.html"
    context_object_name = 'edit_booking'

    def get(self, request, booking_id, *args, **kwargs):
        # queryset = Booking.objects.all()
        booking = get_object_or_404(Booking, pk=booking_id)

        return render(
            request,
            "edit_booking.html",
            {
                "booking": booking,
                "updated": False,
                "Update_BookingDetails": UpdateBookingDetails(instance=booking)
            },
        )

    def post(self, request, booking_id, *args, **kwargs):
        booking = get_object_or_404(Booking, pk=booking_id)

        booking_details_form = UpdateBookingDetails(request.POST, instance=booking)

        if booking_details_form.is_valid():
            booking.status = 0
            booking_updates = booking_details_form.save()
        else:
            booking_details_form = UpdateBookingDetails(instance=booking)

        return render(
            request,
            "edit_booking.html",
            {
                "booking": booking,
                'updated': True,
                "Update_BookingDetails": booking_details_form,
            },
        )
        