from django.db import models
from django.conf import settings

# Create your models here
from institution.models import Institution
from dictionary.models import Dictionary
from generic.models import TimestampUserLogModel


class Case(TimestampUserLogModel):
    comment = models.CharField(max_length=256)
    auditedInstitution = models.ManyToManyField(to=Institution)
    name = models.CharField(max_length=256)
    responsibleUser = models.ManyToManyField(
        to=settings.AUTH_USER_MODEL,
        through='UserRef',
        through_fields=('case', 'user'),
        related_name='case_responsibleUser'
    )
    notifiedUser = models.ManyToManyField(
        to=settings.AUTH_USER_MODEL,
        through='UserRefProxy',
        through_fields=('case', 'user'),
        related_name='case_notifiedUser'
    )

    letterCount = models.IntegerField(default=0)
    noteCount = models.IntegerField(default=0)

    matrix = models.ManyToManyField(to=Dictionary)


class UserRef(models.Model):
    user = models.ForeignKey(to=settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    case = models.ForeignKey(Case, on_delete=models.CASCADE)


class UserRefProxy(UserRef):
    class Meta:
        proxy = True
