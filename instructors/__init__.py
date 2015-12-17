from django.contrib.auth.models import User


def is_instructor(self):
    return hasattr(self, 'instructor')


User.add_to_class("is_instructor", is_instructor)
