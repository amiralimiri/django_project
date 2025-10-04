from django.core import validators
from django.utils.deconstruct import deconstructible
from typing import Callable

@deconstructible
class RegNumberValidator(validators.RegexValidator):
    regex = r'^\d{10}$'
    message = (
        'Enter a valid registration number. This value may contain numbers only, '
        'and must be exactly 10 digits'
    )
    flags = 0


reg_number_validator: Callable[[str], None] = RegNumberValidator()
