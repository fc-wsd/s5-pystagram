# photos/templatetags/my_tags.py

from django import template


register = template.Library()


@register.filter
def did_like(photo, user):
    return photo.like_set.filter(user=user, status=True).exists()

