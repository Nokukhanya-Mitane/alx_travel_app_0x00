#!/usr/bin/env python3
from django.core.management.base import BaseCommand
from listings.models import Listing
import random


class Command(BaseCommand):
    help = "Seed the database with sample listings data"

    def handle(self, *args, **kwargs):
        sample_listings = [
            {
                "title": "Beachfront Villa",
                "description": "Luxury villa with ocean views.",
                "price_per_night": 350.00,
                "location": "Cape Town"
            },
            {
                "title": "City Apartment",
                "description": "Modern apartment in the city center.",
                "price_per_night": 180.00,
                "location": "Johannesburg"
            },
            {
                "title": "Safari Lodge",
                "description": "Experience wildlife in comfort.",
                "price_per_night": 500.00,
                "location": "Kruger National Park"
            }
        ]

        for listing in sample_listings:
            Listing.objects.create(**listing)

        self.stdout.write(self.style.SUCCESS("Successfully seeded listings data!"))
