from django.db import models
from django.contrib.auth.models import User


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
        User,
        on_delete=models.DO_NOTHING,
        related_name='institution_createdBy',
        null=True,
        blank=True
    )
    modifiedBy = models.ForeignKey(
        User,
        on_delete=models.DO_NOTHING,
        related_name='institution_modifiedBy',
        null=True,
        blank=True
    )
    administrativeUnit = models.OneToOneField(AdministrativeUnit, on_delete=models.CASCADE, null=True, blank=True)
    address = models.OneToOneField(AddressData, on_delete=models.CASCADE, null=True, blank=True)


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
        User,
        on_delete=models.DO_NOTHING,
        related_name='channel_createdBy',
        null=True,
        blank=True
    )
    modifiedBy = models.ForeignKey(
        User,
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


class UserRef(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)


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
        User,
        on_delete=models.DO_NOTHING,
        related_name='dictionary_createdBy',
        null=True,
        blank=True
    )
    modifiedBy = models.ForeignKey(
        User,
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
    value = models.CharField(max_length=100)
    dictionary = models.ForeignKey(to=Dictionary, on_delete=models.CASCADE)


class Case(models.Model):
    comment = models.CharField(max_length=256)
    modifiedOn = models.DateTimeField(auto_now=True)
    createdOn = models.DateTimeField(auto_now_add=True)

    name = models.CharField(max_length=256)
    responsibleUser = models.ManyToManyField(to=UserRef, related_name='case_responsibleUser')

    createdBy = models.ForeignKey(
        User,
        on_delete=models.DO_NOTHING,
        related_name='case_createdBy',
        null=True,
        blank=True
    )
    modifiedBy = models.ForeignKey(
        User,
        on_delete=models.DO_NOTHING,
        related_name='case_modifiedBy',
        null=True,
        blank=True
    )
    notifiedUser = models.ManyToManyField(to=UserRef, related_name='case_notifiedUser')
    letterCount = models.IntegerField(default=0)
    noteCount = models.IntegerField(default=0)

    matrix = models.ManyToManyField(to=Dictionary)


class Tag(models.Model):
    tag_field = models.CharField(max_length=256)
    case = models.ForeignKey(to=Case, on_delete=models.CASCADE)


