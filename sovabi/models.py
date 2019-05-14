from django.db import models
from django.utils.translation import ugettext_lazy as _

class SovabiModel:
    added_date = models.DateTimeField(
        _('date added to the database'),
        auto_now_add=True,
        blank=True
    )
    updated_date = models.DateTimeField(
        _('date updated to the database'),
        auto_now=True
    )