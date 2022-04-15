from django.urls import path
from .views import PlatoApiView
from rest_framework_simplejwt.views import TokenObtainPairView

urlpatterns = [
    path('', PlatoApiView.as_view()),
]