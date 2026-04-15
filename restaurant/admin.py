from django.contrib import admin
from .models import Menu, Booking


# Register Menu model with admin site
@admin.register(Menu)
class MenuAdmin(admin.ModelAdmin):
    list_display = ('title', 'price', 'inventory')
    search_fields = ('title',)


# Register Booking model with admin site
@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    list_display = ('name', 'no_of_guests', 'booking_date')
    search_fields = ('name',)
    list_filter = ('booking_date',)
