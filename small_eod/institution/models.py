from django.db import models
from django.conf import settings

# Create your models here.


class AddressData(models.Model):
    city = models.CharField(max_length=100)
    voivodeship = models.CharField(max_length=100)
    flat_no = models.CharField(max_length=100, null=True, blank=True)
    street = models.CharField(max_length=100)
    postal_code = models.CharField(max_length=100)
    house_no = models.CharField(max_length=100)
    email = models.EmailField()
    epuap = models.CharField(max_length=100)


class ExternalIdentifier(models.Model):
    nip = models.CharField(max_length=100)
    regon = models.CharField(max_length=100)


class AdministrativeUnit(models.Model):
    category = models.CharField(max_length=100)
    terc = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    level = models.IntegerField()


class Institution(models.Model):
    name = models.CharField(max_length=256)
    external_identifier = models.OneToOneField(ExternalIdentifier, on_delete=models.CASCADE, null=True, blank=True)
    createdOn = models.DateTimeField(auto_now_add=True)
    modifiedOn = models.DateTimeField(auto_now=True)
    createdBy = models.ForeignKey(
        to=settings.AUTH_USER_MODEL,
        on_delete=models.DO_NOTHING,
        related_name='institution_createdBy',
        null=True,
        blank=True
    )
    modifiedBy = models.ForeignKey(
        to=settings.AUTH_USER_MODEL,
        on_delete=models.DO_NOTHING,
        related_name='institution_modifiedBy',
        null=True,
        blank=True
    )
    administrativeUnit = models.OneToOneField(AdministrativeUnit, on_delete=models.CASCADE, null=True, blank=True)
    address = models.OneToOneField(AddressData, on_delete=models.CASCADE, null=True, blank=True)
