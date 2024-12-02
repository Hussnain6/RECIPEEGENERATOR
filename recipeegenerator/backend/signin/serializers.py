from django.contrib.auth.models import User
from django.db import models
from rest_framework import serializers

# UserProfile model to store additional user details
class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone_number = models.CharField(max_length=15)

# Serializer for the User model
class UserSerializer(serializers.ModelSerializer):
    # Adding a phone_number field
    phone_number = serializers.CharField(write_only=True, required=True)

    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'first_name', 'last_name', 'password', 'phone_number']
        extra_kwargs = {"password": {"write_only": True}}

    def create(self, validated_data):
        # Extract the phone_number before creating the user
        phone_number = validated_data.pop('phone_number', None)

        # Create the user with the remaining data
        user = User.objects.create_user(**validated_data)

        # Save the phone number in the UserProfile model
        UserProfile.objects.create(user=user, phone_number=phone_number)

        return user
