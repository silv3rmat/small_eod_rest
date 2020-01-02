from django.db import models
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
# Create your models here
from institution.models import Institution
from dictionary.models import Dictionary
from django.conf import settings


class Case(models.Model):
    comment = models.CharField(max_length=256)
    modifiedOn = models.DateTimeField(auto_now=True)
    createdOn = models.DateTimeField(auto_now_add=True)
    auditedInstitution = models.ManyToManyField(to=Institution)
    name = models.CharField(max_length=256)
    responsibleUser = models.ManyToManyField(
        to=settings.AUTH_USER_MODEL,
        through='UserRef',
        through_fields=('case', 'user'),
        related_name='case_responsibleUser'
    )
    createdBy = models.ForeignKey(
        to=settings.AUTH_USER_MODEL,
        on_delete=models.DO_NOTHING,
        related_name='case_createdBy',
        null=True,
        blank=True
    )
    modifiedBy = models.ForeignKey(
        to=settings.AUTH_USER_MODEL,
        on_delete=models.DO_NOTHING,
        related_name='case_modifiedBy',
        null=True,
        blank=True
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


class Tag(models.Model):
    limit= models.Q(app_label='case', model='Case') | \
        models.Q(app_label='api', model='Letter')

    tag_field = models.CharField(max_length=256)
    content_type = models.ForeignKey(
        ContentType,
        on_delete=models.CASCADE,
        limit_choices_to= limit
    )
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey('content_type', 'object_id')


class UserRef(models.Model):
    user = models.ForeignKey(to=settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    case = models.ForeignKey(Case, on_delete=models.CASCADE)


class UserRefProxy(UserRef):
    class Meta:
        proxy = True
