from django.db import models
from user.models import MyUser as User
# Create your models here.
from django.conf import settings

class Dictionary(models.Model):
    class Types(models.TextChoices):
        WHOSE = "WHOSE", "whose case"
        WSCOPE = "WSCOPE", "Jaki zakres sprawy"
        ISCOPE = "ISCOPE", "Bezczynność w jakim zakresie"
        DSCOPE = "DSCOPE", "Decyzja w jakim zakresie"
        INFOT = "INFOT", "Informacja udzielona w którym momencie"
        STATUS = "STATUS", "Status"

    modifiedOn = models.DateTimeField(auto_now=True)
    createdOn = models.DateTimeField(auto_now_add=True)
    createdBy = models.ForeignKey(
        to=settings.AUTH_USER_MODEL,
        on_delete=models.DO_NOTHING,
        related_name='dictionary_createdBy',
        null=True,
        blank=True
    )
    modifiedBy = models.ForeignKey(
        to=settings.AUTH_USER_MODEL,
        on_delete=models.DO_NOTHING,
        related_name='dictionary_modifiedBy',
        null=True,
        blank=True
    )
    name = models.CharField(max_length=100, choices=Types.choices)
    minItems = models.IntegerField(default=1)
    maxItems = models.IntegerField(default=1)
    active = models.BooleanField(default=True)


class DictValue(models.Model):
    name = models.CharField(max_length=100)
    value = models.BooleanField(default=False)
    dictionary = models.ForeignKey(to=Dictionary, on_delete=models.CASCADE)
