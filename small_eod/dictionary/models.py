from django.db import models
from generic.models import TimestampUserLogModel


class Dictionary(TimestampUserLogModel):
    class Types(models.TextChoices):
        WHOSE = "WHOSE", "whose case"
        WSCOPE = "WSCOPE", "Jaki zakres sprawy"
        ISCOPE = "ISCOPE", "Bezczynność w jakim zakresie"
        DSCOPE = "DSCOPE", "Decyzja w jakim zakresie"
        INFOT = "INFOT", "Informacja udzielona w którym momencie"
        STATUS = "STATUS", "Status"

    name = models.CharField(max_length=100, choices=Types.choices)
    minItems = models.IntegerField(default=1)
    maxItems = models.IntegerField(default=1)
    active = models.BooleanField(default=True)


class DictValue(models.Model):
    name = models.CharField(max_length=100)
    value = models.BooleanField(default=False)
    dictionary = models.ForeignKey(to=Dictionary, on_delete=models.CASCADE)
