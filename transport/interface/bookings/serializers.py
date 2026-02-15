from rest_framework import serializers

from transport.domain.bookings.models import Bookings


class QuoteSerializer(serializers.Serializer):
    source_city = serializers.CharField(max_length=100)
    destination_city = serializers.CharField(max_length=100)
    weight_kg = serializers.IntegerField(min_value=1)


class BookingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bookings
        fields = "__all__"
