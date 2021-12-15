from . import views
from django.urls import path


urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),
    path('menu/', views.MenuView.as_view(), name='menu'),
    path('contact_us/', views.ContactView.as_view(), name='contact'),
    path('online_bookings/', views.OnlineBookingView.as_view(), name='online_booking'),
    path('edit_profile/', views.EditProfile.as_view(), name='edit_profile'),
    path('manage_booking/', views.ManageBooking.as_view(), name='manage_booking'),
    path('edit_booking/<str:booking_id>/', views.EditBooking.as_view(), name='edit_booking'),
]