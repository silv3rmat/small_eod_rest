from django.contrib import admin

# Register your models here.
from api.models import AdministrativeUnit, Institution, AddressData, ExternalIdentifier

admin.site.register(Institution)
admin.site.register(AdministrativeUnit)
admin.site.register(AddressData)
admin.site.register(ExternalIdentifier)