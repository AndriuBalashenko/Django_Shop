from django import template

register = template.Library()


@register.filter
def view_rating(numb):
    """Добавление символа в рейтига продукта"""
    return int(numb) * '🌻'
