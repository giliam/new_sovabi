from django.db import models
from django.utils.translation import ugettext_lazy as _

from sovabi.models import SovabiModel


class Lieu(models.Model, SovabiModel):    
    nom = models.CharField(max_length=150, blank=False)

    def __str__(self):
        return u"{0}".format(self.nom)

    class Meta:
        verbose_name_plural = "Lieux"


class TypeCelebration(models.Model, SovabiModel):    
    nom = models.CharField(max_length=150, blank=False)

    def __str__(self):
        return u"{0}".format(self.nom)

    class Meta:
        verbose_name = "Type de célébration"
        verbose_name_plural = "Types de célébration"


class Messe(models.Model, SovabiModel):
    messe_date = models.DateField(
        _('date of the mass')
    )
    lieu = models.ForeignKey(
        'Lieu', 
        on_delete=models.SET_DEFAULT, default=0, null=False, related_name="messes"
    )
    type_celebration = models.ForeignKey(
        'TypeCelebration', 
        on_delete=models.SET_DEFAULT, default=0, null=False, related_name="messes"
    )

    def __str__(self):
        return u"{0}".format(self.messe_date)