from transport.domain.bookings.models import Bookings
from transport.domain.users.models import RoleChoices


class BookingDomainService:

    def create_booking(self, user, data):
        booking = Bookings.objects.create(
            customer=user,
            source_city=data["source_city"],
            destination_city=data["destination_city"],
            weight_kp=data["weight_kp"],
            final_price=data["final_price"],
        )
        return booking

    def get_bookings(self, user):
        if user.role == RoleChoices.ADMIN:
            return Bookings.objects.all()
        return Bookings.objects.filter(customer=user)
