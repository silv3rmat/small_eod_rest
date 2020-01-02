from django.db import models
from user.models import MyUser as User
# from model_utils.models import TimeStampedModel


class Error(models.Model):
    message = models.CharField(max_length=512)
    code = models.IntegerField(unique=True)


class TagNamespace(models.Model):
    description = models.CharField(max_length=256)
    color = models.CharField(max_length=9, default='0000000000')
    modifiedOn = models.DateTimeField(auto_now=True)
    createdOn = models.DateTimeField(auto_now_add=True)
    createdBy = models.ForeignKey(
        User,
        on_delete=models.DO_NOTHING,
        related_name='tag_createdBy',
        null=True,
        blank=True
    )
    modifiedBy = models.ForeignKey(
        User,
        on_delete=models.DO_NOTHING,
        related_name='tag_modifiedBy',
        null=True,
        blank=True
    )


class Letter(models.Model):

    class Direction(models.TextChoices):
        IN = 'IN', 'Received'
        OUT = 'OUT', 'Sent'

    modifiedOn = models.DateTimeField(auto_now=True)
    createdOn = models.DateTimeField(auto_now_add=True)
    createdBy = models.ForeignKey(
        User,
        on_delete=models.DO_NOTHING,
        related_name='letter_createdBy',
        null=True,
        blank=True
    )
    modifiedBy = models.ForeignKey(
        User,
        on_delete=models.DO_NOTHING,
        related_name='letter_modifiedBy',
        null=True,
        blank=True
    )
    direction = models.TextField(choices=Direction.choices, default=Direction.IN, max_length=3)
