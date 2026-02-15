from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework_simplejwt.authentication import JWTAuthentication

from transport.application.bookings.services import BookingAppService
from transport.domain.users.models import RoleChoices
from transport.utils.response import ErrorResponse, SuccessResponse

from .serializers import BookingSerializer, QuoteSerializer


class QuoteAPIView(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    def __init__(self):
        self.booking_app_service = BookingAppService()

    def post(self, request):
        """
        Process a quote.

        Args:
            request: The incoming request object.

        Returns:
            SuccessResponse: If the quote was processed successfully, containing the processed quote data and a success message.
            ErrorResponse: If the quote processing failed, containing the error and a failure message.
        """
        serializer = QuoteSerializer(data=request.data)
        if serializer.is_valid():
            result = self.booking_app_service.process_quote(data=serializer.data)
            return SuccessResponse(data=result, message="Quote processed successfully")
        return ErrorResponse(error=serializer.errors, message="Quote processing failed")


class BookingsAPIViewSet(viewsets.ModelViewSet):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
    serializer_class = BookingSerializer

    def __init__(self):
        self.booking_app_service = BookingAppService()

    def create(self, request, *args, **kwargs):
        """
        Creates a new booking based on the provided data.

        Args:
            request: The incoming request object.
            *args: Any additional positional arguments.
            **kwargs: Any additional keyword arguments.

        Returns:
            SuccessResponse: If the booking was created successfully, containing the created booking data and a success message.
            ErrorResponse: If the booking creation failed, containing the error and a failure message.
        """
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            result = self.booking_app_service.create_booking(data=serializer.data)
            return SuccessResponse(data=result, message="Booking created successfully")
        return ErrorResponse(error=serializer.errors, message="Booking creation failed")

    def get_queryset(self, request, *args, **kwargs):
        """
        Returns a queryset of bookings based on the current user.

        If the current user is an admin, all bookings are returned.
        If the current user is not an admin, only the bookings belonging to the user are returned.
        """
        user = self.request.user
        return self.booking_app_service.get_bookings(user=user)

    def partial_update(self, request, *args, **kwargs):
        """
        Updates the status of a booking based on the provided data.

        Args:
            request: The incoming request object.
            *args: Any additional positional arguments.
            **kwargs: Any additional keyword arguments.

        Returns:
            SuccessResponse: If the status was updated successfully, containing the updated booking data and a success message.
            ErrorResponse: If the status update failed, containing the error and a failure message.

        Note: Only administrators are authorized to update the status of bookings.
        """
        if request.user.role == RoleChoices.ADMIN:
            result = self.partial_update(request, *args, **kwargs)
            return SuccessResponse(data=result, message="Status updated successfully")
        return ErrorResponse(
            error="You are not authorized to update this status",
            message="Status update failed",
        )
