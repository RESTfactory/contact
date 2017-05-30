from django.contrib import admin
from .models import (
    ContactCreator,
    ContactType,
    ContactInfo
)

admin.site.register(ContactCreator)
admin.site.register(ContactType)
admin.site.register(ContactInfo)
