from rest_framework import serializers
from .models import Menu, Booking


class MenuSerializer(serializers.ModelSerializer):
    """Serializer for the Menu model."""

    class Meta:
        model = Menu
        fields = '__all__'


class BookingSerializer(serializers.ModelSerializer):
    """Serializer for the Booking model."""

    class Meta:
        model = Booking
        fields = '__all__'
