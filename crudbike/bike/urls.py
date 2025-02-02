from django.urls import path
from .views import home, RegisterView, LoginView, BikeListCreateView, BikeDetailView

urlpatterns = [
    #Django Template Langauge
    path('', home, name='home'),
    # Auth Endpoints
    path('api/register/', RegisterView.as_view(), name='register'),
    path('api/login/', LoginView.as_view(), name='login'),

    # Bike CRUD Endpoints
    path('api/bikes/', BikeListCreateView.as_view(), name='bike-list-create'),
    path('api/bikes/<int:pk>/', BikeDetailView.as_view(), name='bike-detail'),
]
