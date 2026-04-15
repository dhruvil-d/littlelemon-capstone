from django.test import TestCase
from restaurant.models import Menu, Booking
from datetime import datetime
from django.utils.timezone import make_aware


class MenuModelTest(TestCase):
    """Unit tests for the Menu model."""

    def setUp(self):
        """Create a test menu item."""
        self.menu_item = Menu.objects.create(
            title='IceCream',
            price=80,
            inventory=100,
        )

    def test_menu_item_creation(self):
        """Test that a menu item is created correctly."""
        self.assertEqual(self.menu_item.title, 'IceCream')
        self.assertEqual(self.menu_item.price, 80)
        self.assertEqual(self.menu_item.inventory, 100)

    def test_menu_str(self):
        """Test the string representation of a menu item."""
        self.assertEqual(str(self.menu_item), 'IceCream : 80')

    def test_menu_item_count(self):
        """Test that the correct number of menu items exist."""
        Menu.objects.create(title='Pizza', price=150, inventory=50)
        self.assertEqual(Menu.objects.count(), 2)

    def test_menu_item_update(self):
        """Test updating a menu item."""
        self.menu_item.price = 100
        self.menu_item.save()
        updated_item = Menu.objects.get(id=self.menu_item.id)
        self.assertEqual(updated_item.price, 100)

    def test_menu_item_delete(self):
        """Test deleting a menu item."""
        item_id = self.menu_item.id
        self.menu_item.delete()
        self.assertFalse(Menu.objects.filter(id=item_id).exists())


class BookingModelTest(TestCase):
    """Unit tests for the Booking model."""

    def setUp(self):
        """Create a test booking."""
        self.booking_date = make_aware(datetime(2024, 6, 15, 18, 0, 0))
        self.booking = Booking.objects.create(
            name='John Doe',
            no_of_guests=4,
            booking_date=self.booking_date,
        )

    def test_booking_creation(self):
        """Test that a booking is created correctly."""
        self.assertEqual(self.booking.name, 'John Doe')
        self.assertEqual(self.booking.no_of_guests, 4)
        self.assertEqual(self.booking.booking_date, self.booking_date)

    def test_booking_str(self):
        """Test the string representation of a booking."""
        self.assertIn('John Doe', str(self.booking))

    def test_booking_count(self):
        """Test that the correct number of bookings exist."""
        new_date = make_aware(datetime(2024, 7, 20, 19, 0, 0))
        Booking.objects.create(name='Jane', no_of_guests=2, booking_date=new_date)
        self.assertEqual(Booking.objects.count(), 2)

    def test_booking_update(self):
        """Test updating a booking."""
        self.booking.no_of_guests = 6
        self.booking.save()
        updated = Booking.objects.get(id=self.booking.id)
        self.assertEqual(updated.no_of_guests, 6)

    def test_booking_delete(self):
        """Test deleting a booking."""
        booking_id = self.booking.id
        self.booking.delete()
        self.assertFalse(Booking.objects.filter(id=booking_id).exists())
