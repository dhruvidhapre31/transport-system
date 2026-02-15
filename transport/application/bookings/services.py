import random

from transport.domain.bookings.services import BookingDomainService


class BookingAppService:

    def __init__(self):
        self.booking_domain_service = BookingDomainService()

    def process_quote(self, data):
        weight_kg = data.get("weight_kg")
        distance_km = random.randint(50, 500)
        base_price = distance_km * 5
        final_price = base_price + (weight_kg * 2)
        return {
            "distance_km": distance_km,
            "base_price": base_price,
            "final_price": final_price,
        }

    def create_booking(self, user, data):
        return self.booking_domain_service.create_booking(user, data)

    def get_bookings(self, user):
        return self.booking_domain_service.get_bookings(user)
