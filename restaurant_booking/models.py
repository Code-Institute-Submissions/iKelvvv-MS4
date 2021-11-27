from django.db import models

# Import Django authentication user system
from django.contrib.auth.models import User
#Import cloudinary for featured image
from cloudinary.models import CloudinaryField

# Create your models here.
STATUS = ((0, "Booking Requested"), (1, "Booking Accepted"))

class Booking(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    booking_date = models.DateField(auto_now=False)
    booking_time = models.TimeField(auto_now=False)
    booking_comments = models.TextField()
    guest_count = models.IntegerField()
    status = models.IntegerField(choices=STATUS, default=0)

    # Django magic method to return string represention of an object
    def __str__(self):
        return self.title
