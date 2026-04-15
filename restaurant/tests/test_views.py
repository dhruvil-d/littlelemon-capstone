from django.test import TestCase
from django.contrib.auth.models import User
from rest_framework.test import APIClient
from rest_framework import status
from restaurant.models import Menu, Booking
from datetime import datetime
from django.utils.timezone import make_aware


class MenuViewTest(TestCase):
    """API tests for the Menu endpoints."""

    def setUp(self):
        """Set up test client with authenticated user and sample data."""
        self.client = APIClient()
        self.user = User.objects.create_user(
            username='testuser',
            password='testpass123',
        )
        self.client.force_authenticate(user=self.user)

        self.menu_item = Menu.objects.create(
            title='Pasta',
            price=12.99,
            inventory=50,
        )

    def test_get_menu_list(self):
        """Test retrieving the list of menu items."""
        response = self.client.get('/api/menu/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)

    def test_get_menu_detail(self):
        """Test retrieving a single menu item."""
        response = self.client.get(f'/api/menu/{self.menu_item.id}/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['title'], 'Pasta')

    def test_create_menu_item(self):
        """Test creating a new menu item."""
        data = {'title': 'Burger', 'price': 8.50, 'inventory': 30}
        response = self.client.post('/api/menu/', data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Menu.objects.count(), 2)
        self.assertEqual(response.data['title'], 'Burger')

    def test_update_menu_item(self):
        """Test updating an existing menu item."""
        data = {'title': 'Pasta Deluxe', 'price': 15.99, 'inventory': 40}
        response = self.client.put(
            f'/api/menu/{self.menu_item.id}/', data, format='json'
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.menu_item.refresh_from_db()
        self.assertEqual(self.menu_item.title, 'Pasta Deluxe')

    def test_delete_menu_item(self):
        """Test deleting a menu item."""
        response = self.client.delete(f'/api/menu/{self.menu_item.id}/')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Menu.objects.count(), 0)

    def test_unauthenticated_access(self):
        """Test that unauthenticated requests are rejected."""
        self.client.force_authenticate(user=None)
        response = self.client.get('/api/menu/')
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)


class BookingViewTest(TestCase):
    """API tests for the Booking endpoints."""

    def setUp(self):
        """Set up test client with authenticated user and sample data."""
        self.client = APIClient()
        self.user = User.objects.create_user(
            username='testuser',
            password='testpass123',
        )
        self.client.force_authenticate(user=self.user)

        self.booking_date = make_aware(datetime(2024, 8, 20, 19, 30, 0))
        self.booking = Booking.objects.create(
            name='Alice Smith',
            no_of_guests=3,
            booking_date=self.booking_date,
        )

    def test_get_booking_list(self):
        """Test retrieving the list of bookings."""
        response = self.client.get('/api/bookings/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)

    def test_get_booking_detail(self):
        """Test retrieving a single booking."""
        response = self.client.get(f'/api/bookings/{self.booking.id}/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['name'], 'Alice Smith')

    def test_create_booking(self):
        """Test creating a new booking."""
        data = {
            'name': 'Bob Jones',
            'no_of_guests': 5,
            'booking_date': '2024-09-10T20:00:00Z',
        }
        response = self.client.post('/api/bookings/', data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Booking.objects.count(), 2)

    def test_update_booking(self):
        """Test updating an existing booking."""
        data = {
            'name': 'Alice Smith',
            'no_of_guests': 6,
            'booking_date': '2024-08-20T19:30:00Z',
        }
        response = self.client.put(
            f'/api/bookings/{self.booking.id}/', data, format='json'
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.booking.refresh_from_db()
        self.assertEqual(self.booking.no_of_guests, 6)

    def test_delete_booking(self):
        """Test deleting a booking."""
        response = self.client.delete(f'/api/bookings/{self.booking.id}/')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Booking.objects.count(), 0)

    def test_unauthenticated_access(self):
        """Test that unauthenticated requests are rejected."""
        self.client.force_authenticate(user=None)
        response = self.client.get('/api/bookings/')
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
