from django.db import models

# Import Django authentication user system
from django.contrib.auth.models import User
# Import cloudinary for featured image
from cloudinary.models import CloudinaryField


# Create your models here.
STATUS = ((0, "Booking Requested"), (1, "Booking Accepted"))


class Booking(models.Model):
    title = models.CharField(max_length=200, default='Booking Request')
    user_id = models.ForeignKey(User, on_delete=models.CASCADE, related_name="user_bookings")
    booking_date = models.DateField(auto_now=False)
    booking_time = models.TimeField(auto_now=False)
    booking_comments = models.TextField(max_length=200, blank=True, default='Please note any allergies')
    created_on = models.DateTimeField(auto_now_add=True)
    guest_count = models.IntegerField()
    status = models.IntegerField(choices=STATUS, default=0)

    class Meta:
        ordering = ['-created_on']

    # Django magic method to return string represention of an object
    def __str__(self):
        return self.title
