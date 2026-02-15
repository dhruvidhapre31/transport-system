from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .views import BookingsAPIViewSet, QuoteAPIView

router = DefaultRouter()
router.register(r"bookings", BookingsAPIViewSet, basename="bookings")

urlpatterns = [
    path("quote/", QuoteAPIView.as_view(), name="quote"),
    path("", include(router.urls)),
]
