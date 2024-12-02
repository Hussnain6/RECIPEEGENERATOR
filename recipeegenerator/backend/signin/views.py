from django.shortcuts import render
from django.contrib.auth.models import User
from rest_framework import generics
from .serializers import UserSerializer
from rest_framework.permissions import AllowAny

# Create your signup view here
class UserView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer  # Use the serializer, not the model
    permission_classes = [AllowAny]  # Allow any user to access the signup endpoint
