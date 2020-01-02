from django.contrib import admin

# Register your models here.
from collection.models import Collection, Letter, Note, Event, CollectionCollectable

admin.site.register(Collection)
admin.site.register(Letter)
admin.site.register(Note)
admin.site.register(Event)
admin.site.register(CollectionCollectable)