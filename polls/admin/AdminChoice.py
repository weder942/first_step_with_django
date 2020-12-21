from django.contrib import admin
from ..models import Choice


class ChoiceInline(admin.TabularInline):
    """

    """
    model = Choice
    extra = 3
