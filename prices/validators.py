# prices/validators.py
import re
from django.core.exceptions import ValidationError

def validate_username(value):
    if not re.search(r'[A-Z]', value):  # Verifica si contiene al menos una mayúscula
        raise ValidationError('El nombre de usuario debe contener al menos una letra mayúscula.')
    if not re.search(r'[0-9]', value):  # Verifica si contiene al menos un número
        raise ValidationError('El nombre de usuario debe contener al menos un número.')
