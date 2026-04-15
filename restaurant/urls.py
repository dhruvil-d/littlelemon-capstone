from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework.authtoken.views import obtain_auth_token
from . import views

# Create and register DRF routers
router = DefaultRouter()
router.register(r'menu', views.MenuViewSet, basename='menu')
router.register(r'bookings', views.BookingViewSet, basename='bookings')

urlpatterns = [
    path('', views.index, name='index'),
    path('api/', include(router.urls)),
    path('api-token-auth/', obtain_auth_token, name='api_token_auth'),
]
