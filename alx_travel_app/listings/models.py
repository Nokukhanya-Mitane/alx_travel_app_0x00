#!/usr/bin/env python3
from django.db import models
import uuid


class Listing(models.Model):
    """Listing Model"""
    listing_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField(max_length=255)
    description = models.TextField()
    price_per_night = models.DecimalField(max_digits=10, decimal_places=2)
    location = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class Booking(models.Model):
    """Booking Model"""
    booking_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    listing = models.ForeignKey(Listing, related_name="bookings", on_delete=models.CASCADE)
    customer_name = models.CharField(max_length=255)
    check_in = models.DateField()
    check_out = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Booking for {self.customer_name} - {self.listing.title}"


class Review(models.Model):
    """Review Model"""
    review_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    listing = models.ForeignKey(Listing, related_name="reviews", on_delete=models.CASCADE)
    rating = models.IntegerField()
    comment = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        constraints = [
            models.CheckConstraint(
                check=models.Q(rating__gte=1, rating__lte=5),
                name="rating_range_1_to_5"
            )
        ]

    def __str__(self):
        return f"Review {self.rating} stars"
