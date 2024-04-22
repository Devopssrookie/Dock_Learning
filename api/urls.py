from django.urls import path
from . import views

from rest_framework_simplejwt.views import (         ## from simple jwt documentation
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [
    path('users/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('users/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

    path('',views.getroutes),         ##api url mapping, root empty url maps anything we enter 
    path('members/search/', views.search_members),
    path('members/create/', views.postmember),  # Endpoint to create a new member
    path('members/<str:pk>/', views.getmember),  # Endpoint to retrieve a specific member
    path('members/<str:pk>/update/', views.updatemember),              #Endpoint to update
    path('members/', views.getmembers),
    path('members/<str:pk>/delete/', views.deletemember),
]


