from django.core.exceptions import ValidationError
import re


def validate_phone_number(value):
    if not re.match(r'^\d+$', value):
        raise ValidationError("Phone number must be numeric.")