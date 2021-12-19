import uuid
from django.db import models
# Import Django authentication user system
from django.contrib.auth.models import User
# Import cloudinary for featured image
from cloudinary.models import CloudinaryField


# Create your models here.
STATUS = ((0, "Booking Requested"), (1, "Booking Accepted"))


class Booking(models.Model):
    booking_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="user_bookings")
    booking_date = models.DateField(auto_now=False)
    booking_time = models.TimeField(auto_now=False)
    booking_comments = models.TextField(max_length=200, blank=True)
    created_on = models.DateTimeField(auto_now_add=True)
    guest_count = models.IntegerField()
    status = models.IntegerField(choices=STATUS, default=0)

    class Meta:
        ordering = ['-booking_date']