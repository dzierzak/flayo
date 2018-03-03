from django import template
from django.contrib.auth.models import Group


# It's a templatetag which check group of current logged user
register = template.Library()


@register.filter(name='user_has_group')
def user_has_group(user, group_name):
    group = Group.objects.get(name=group_name)
    return group in user.groups.all()




