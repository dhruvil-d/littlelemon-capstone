from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from .models import Menu, Booking
from .serializers import MenuSerializer, BookingSerializer


def index(request):
    """Serve the static index.html template."""
    return render(request, 'index.html', {})


class MenuViewSet(viewsets.ModelViewSet):
    """ViewSet providing CRUD operations for Menu items."""
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer
    permission_classes = [IsAuthenticated]


class BookingViewSet(viewsets.ModelViewSet):
    """ViewSet providing CRUD operations for Bookings."""
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer
    permission_classes = [IsAuthenticated]
