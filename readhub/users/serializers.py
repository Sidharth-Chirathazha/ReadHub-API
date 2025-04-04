from rest_framework import serializers
import logging
from django.contrib.auth import get_user_model
from .validators import email_validator,username_validator,password_validator
from django.contrib.auth import authenticate
from rest_framework_simplejwt.tokens import RefreshToken

User = get_user_model()
logger = logging.getLogger(__name__) 

class RegistrationSerializer(serializers.ModelSerializer):
    confirm_password = serializers.CharField(write_only = True)

    class Meta:
        model = User
        fields = ["username", "email", "password", "confirm_password"]
        extra_kwargs = {
            "password": {"write_only": True},
        }

    def validate_username(self, value):
        username_validator(value)
        if User.objects.filter(username=value).exists():
            raise serializers.ValidationError("Username is already taken")
        return value
    
    def validate_email(self, value):
        email_validator(value)
        if User.objects.filter(email=value).exists():
            raise serializers.ValidationError("Email already exists")
        return value
    
    def validate_password(self, value):
        password_validator(value)
        return value
    
    def validate(self, data):
        if data["password"] != data["confirm_password"]:
            raise serializers.ValidationError("Passwords doesn't match")
        return data
    
    def create(self, validated_data):
        validated_data.pop("confirm_password")
        user = User.objects.create_user(**validated_data)
        return user
    

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["id", "username", "email"]
    

class LoginSerializer(serializers.Serializer):

    username = serializers.CharField()
    password = serializers.CharField(write_only=True)

    def validate(self, data):
        user = authenticate(username=data["username"], password=data["password"])
        
        if user is None:
            raise serializers.ValidationError("Invalid credentials. Please try again")
        if not user.is_active:
            raise serializers.ValidationError("Your account has been deactivated. Please contact support")
        
        return user
    
class LogoutSerializer(serializers.Serializer):
    refresh = serializers.CharField()

    def validate(self, data):
        try:
            logger.info(f"Received Refresh Token: {data['refresh']}")
            token = RefreshToken(data["refresh"])
            token.blacklist()
        except Exception as e:
            logger.error(f"Error blacklisting token: {str(e)}")
            raise serializers.ValidationError("Invalid refresh token.")
        return data