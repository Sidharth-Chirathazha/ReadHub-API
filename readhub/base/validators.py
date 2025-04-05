import re
from django.core.exceptions import ValidationError
from django.utils.timezone import now
from rest_framework import serializers


def username_validator(username):
    if not re.match(r"^[A-Za-z][A-Za-z0-9]*$", username):
        raise serializers.ValidationError("Username must start with a letter and contain only letters and numbers.")
    
def email_validator(email):
    if not re.match(r"^[\w\.-]+@[\w\.-]+\.\w+$", email):
        raise serializers.ValidationError("Enter a valid email address.")
    
def password_validator(password):
    if len(password) < 5:
        raise serializers.ValidationError("Password must be at least 5 characters long.")
    if " " in password:
        raise serializers.ValidationError("Password cannot contain spaces.")
    
def author_validator(value):
        """Ensure author names contain only alphabets and are not empty"""
        for author in value:
            if not author["name"].strip():
                raise serializers.ValidationError("Author name cannot be empty.")
            if not re.match(r"^[A-Za-z\s]+$", author["name"]):
                raise serializers.ValidationError("Author name can only contain alphabets and spaces.")
        return value

def text_validator(value, field):
    """Ensure text fields starts with an alphabet and does not start with spaces or special characters"""
    if not re.match(r"^[A-Za-z]", value):
        raise serializers.ValidationError(f"{field} must start with an alphabet.")
    

def date_validator(value):
    if value > now().date():
            raise serializers.ValidationError("Publication date cannot be in the future.")