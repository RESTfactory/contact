"""Contact models."""
from django.db import models
from companies.models import (
    App,
    OrganizationalUnitType,
    OrganizationalUnit
)

class ContactCreator(models.Model):
    name = models.CharField(max_length=100)
    contact_name = models.CharField(max_length=100, null=True)
    contact_cellphone = models.CharField(max_length=15, null=True)
    contact_email = models.CharField(max_length=254)
    description = models.CharField(max_length=100)
    app = models.ForeignKey(App)

    class Meta:
        unique_together = ("contact_email", "app")

    def __str__(self):
        return self.name


class ContactType(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=100)
    organizational_unit = models.ForeignKey(OrganizationalUnit)

    def __str__(self):
        return self.name


class ContactInfo(models.Model):
    name = models.CharField(max_length=100)
    contact_name = models.CharField(max_length=100, null=True)
    contact_cellphone = models.CharField(max_length=15, null=True)
    contact_email = models.CharField(max_length=254)
    creator = models.ForeignKey(ContactCreator)
    contact_type = models.ForeignKey(ContactType)
    organizational_unit = models.ForeignKey(OrganizationalUnit)

    def __str__(self):
        return self.name
