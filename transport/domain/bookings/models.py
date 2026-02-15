from django.db import models

from ..users.models import User


class StatusChoices(models.TextChoices):
    PENDING = "PENDING"
    CONFIRMED = "CONFIRMED"
    COMPLETED = "COMPLETED"
    CANCELLED = "CANCELLED"


class Bookings(models.Model):
    customer = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="bookings"
    )
    source_city = models.CharField(max_length=100)
    destination_city = models.CharField(max_length=100)
    weight_kp = models.PositiveIntegerField()
    final_price = models.PositiveIntegerField()
    status = models.CharField(
        max_length=100, choices=StatusChoices.choices, default=StatusChoices.PENDING
    )

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.customer} - {self.source_city} to {self.destination_city}"
