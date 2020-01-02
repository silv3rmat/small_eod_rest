from django.db import models
from django.conf import settings
# Create your models here.


class Required(models.Model):
    city = models.BooleanField()
    voivodeship = models.BooleanField()
    flat_no = models.BooleanField()
    street = models.BooleanField()
    postal_code = models.BooleanField()
    house_no = models.BooleanField()
    email = models.BooleanField()
    epuap = models.BooleanField()


class Channel(models.Model):

    class Name(models.TextChoices):
        FED = 'FED', 'fedrowanie'
        FAX = 'FAX', 'faks'
        CUS = 'CUS', 'od klienta'
        MEC = 'MEC', 'mecenas zewnętrzny'
        PER = 'PER', 'dostarczenie osobiste'
        EMAIL = 'EMAIL', 'email'
        POST = 'POST', 'poczta tradycyjna'
        EPUAP = 'EPUAP', 'epuap'

    modifiedOn = models.DateTimeField(auto_now=True)
    createdOn = models.DateTimeField(auto_now_add=True)
    createdBy = models.ForeignKey(
        to=settings.AUTH_USER_MODEL,
        on_delete=models.DO_NOTHING,
        related_name='channel_createdBy',
        null=True,
        blank=True
    )
    modifiedBy = models.ForeignKey(
        to=settings.AUTH_USER_MODEL,
        on_delete=models.DO_NOTHING,
        related_name='channel_modifiedBy',
        null=True,
        blank=True
    )
    name = models.CharField(
        choices=Name.choices,
        default=Name.EMAIL,
        max_length=5
    )
    required = models.OneToOneField(to=Required, on_delete=models.CASCADE)

