from django.db import models
from apps.users.models import User


# Create your models here.
class Sections(models.Model):
    title = models.CharField(
        max_length=50,
        db_index=True,
    )
    owner = models.ForeignKey(
        to=User,
        null=False,
        blank=False,
        on_delete=models.CASCADE
    )
    parent = models.ForeignKey(
        'self',
        null=True,
        blank=True,
        related_name='subsections',
        on_delete=models.PROTECT
    )

    class Meta:
        verbose_name = 'Section'
        verbose_name_plural = 'Sections'

    def __str__(self) -> str:
        return self.title
