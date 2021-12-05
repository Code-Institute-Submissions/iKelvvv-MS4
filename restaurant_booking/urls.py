from . import views
from django.urls import path


urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),
    path('menu/', views.MenuView.as_view(), name='menu'),
    path('my_booking_details/', views.BookingDetailsView.as_view(), name='booking_detail'),
    path('contact_us/', views.ContactView.as_view(), name='contact'),
    path('online_bookings/', views.OnlineBookingView.as_view(), name='online_booking'),
]