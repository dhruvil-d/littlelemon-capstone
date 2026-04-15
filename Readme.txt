============================================
  Little Lemon Restaurant API - README
============================================

Project: littlelemon
App:     restaurant

--------------------------------------------
SETUP INSTRUCTIONS
--------------------------------------------

1. Install dependencies:
   pip install -r requirements.txt

2. Create MySQL database "littlelemon":
   mysql -u root -p
   CREATE DATABASE littlelemon;

3. Update database credentials in:
   littlelemon/settings.py → DATABASES

4. Run migrations:
   python manage.py migrate

5. Create superuser:
   python manage.py createsuperuser

6. Run the development server:
   python manage.py runserver

--------------------------------------------
API ENDPOINTS
--------------------------------------------

Menu (CRUD):
  GET    /api/menu/          - List all menu items
  POST   /api/menu/          - Create a menu item
  GET    /api/menu/{id}/     - Retrieve a menu item
  PUT    /api/menu/{id}/     - Update a menu item
  DELETE /api/menu/{id}/     - Delete a menu item

Bookings (CRUD):
  GET    /api/bookings/          - List all bookings
  POST   /api/bookings/          - Create a booking
  GET    /api/bookings/{id}/     - Retrieve a booking
  PUT    /api/bookings/{id}/     - Update a booking
  DELETE /api/bookings/{id}/     - Delete a booking

Authentication:
  POST   /api-token-auth/        - Obtain auth token
  POST   /auth/users/            - Register new user
  POST   /auth/token/login/      - Djoser token login
  POST   /auth/token/logout/     - Djoser token logout

Static Page:
  GET    /                       - Home page (index.html)

Admin:
  GET    /admin/                 - Django admin panel

--------------------------------------------
AUTHENTICATION
--------------------------------------------

All /api/ endpoints require Token Authentication.

To authenticate:
1. Register: POST /auth/users/ with username & password
2. Login:    POST /auth/token/login/ to receive token
3. Use header: Authorization: Token <your_token>

--------------------------------------------
RUNNING TESTS
--------------------------------------------

python manage.py test restaurant

--------------------------------------------
TECH STACK
--------------------------------------------

- Python 3.x
- Django 4.2
- Django REST Framework
- Djoser (authentication)
- MySQL

============================================
