import re
from django.core.exceptions import ValidationError


def username_validator(username):
    if not re.match(r"^[A-Za-z][A-Za-z0-9]*$", username):
        raise ValidationError("Username must start with a letter and contain only letters and numbers.")
    
def email_validator(email):
    if not re.match(r"^[\w\.-]+@[\w\.-]+\.\w+$", email):
        raise ValidationError("Enter a valid email address.")
    
def password_validator(password):
    if len(password) < 5:
        raise ValidationError("Password must be at least 5 characters long.")
    if " " in password:
        raise ValidationError("Password cannot contain spaces.")