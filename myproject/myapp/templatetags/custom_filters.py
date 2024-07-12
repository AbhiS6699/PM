# myapp/templatetags/custom_filters.py

from django import template

register = template.Library()

@register.filter
def format_price(value):
    try:
        value = float(value)
    except (ValueError, TypeError):
        return value

    if value >= 10000000:
        return f'{value / 10000000:.2f} Cr'
    elif value >= 100000:
        return f'{value / 100000:.2f} Lac'
    else:
        return f'{value:.2f}'
