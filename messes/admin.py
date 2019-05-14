from django.contrib import admin

from messes.models import (
    Lieu,
    TypeCelebration,
    Messe
)

admin.site.register(Lieu)
admin.site.register(TypeCelebration)
admin.site.register(Messe)