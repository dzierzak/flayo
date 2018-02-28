from django.core.exceptions	import ValidationError


def validate_salary(value):
    if value < 500:
        raise ValidationError("{} is too small salary".format(value))