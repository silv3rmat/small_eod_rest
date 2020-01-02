from django.db import models

# Create your models here.
from django.contrib.contenttypes.fields import GenericForeignKey, GenericRelation
from django.contrib.contenttypes.models import ContentType



from generic.models import TimestampUserLogModel
from channel.models import Channel
from institution.models import Institution, AddressData
from case.models import Case
from files.models import File



class Letter(TimestampUserLogModel):

    class Direction(models.TextChoices):
        IN = 'IN', 'Received'
        OUT = 'OUT', 'Sent'

    direction = models.TextField(choices=Direction.choices, default=Direction.IN, max_length=3)
    name = models.CharField(max_length=256)
    channel = models.ForeignKey(to=Channel, on_delete=models.DO_NOTHING)
    final = models.BooleanField()
    date = models.DateTimeField()
    identifier = models.CharField(max_length=256)
    institution = models.ForeignKey(to=Institution, on_delete=models.DO_NOTHING)
    address = models.ForeignKey(to=AddressData, on_delete=models.DO_NOTHING)
    case = models.ForeignKey(to=Case, on_delete=models.DO_NOTHING)
    attachment = models.ManyToManyField(to=File)
    ordering = models.IntegerField(default=0)
    comment = models.CharField(max_length=256)
    excerpt = models.CharField(max_length=256)


class Note(TimestampUserLogModel):
    case = models.ForeignKey(to=Case, on_delete=models.DO_NOTHING)
    comment = models.CharField(max_length=256)


class Event(TimestampUserLogModel):
    case = models.ForeignKey(to=Case, on_delete=models.DO_NOTHING)
    name = models.CharField(max_length=256)
    data = models.DateTimeField()
    comment = models.CharField(max_length=256)


class Collection(TimestampUserLogModel):

    comment = models.CharField(max_length=256)
    public = models.BooleanField(default=False)
    expiredOn = models.DateTimeField()
    query = models.CharField(max_length=256)


class CollectionCollectable(models.Model):
    limit = models.Q(app_label='collection', model='Event') | \
            models.Q(app_label='collection', model='Note') | \
            models.Q(app_label='collection', model='Letter')

    name = models.CharField(max_length=256)
    content_type = models.ForeignKey(
        ContentType,
        limit_choices_to=limit,
        on_delete=models.DO_NOTHING
    )
    content_id = models.PositiveIntegerField()
    content_object = GenericForeignKey('content_type', 'content_id')
    collection = models.ForeignKey(to=Collection, on_delete=models.DO_NOTHING)
