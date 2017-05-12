"""Contact models."""
from django.db import models


class ContactCreator(models.Model):
    name = models.CharField(max_length=100)
    contact_name = models.CharField(max_length=100, null=True)
    contact_cellphone = models.CharField(max_length=15, null=True)
    contact_email = models.CharField(max_length=254)
    description = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class ContactType(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class ContactInfo(models.Model):
    name = models.CharField(max_length=100)
    contact_name = models.CharField(max_length=100, null=True)
    contact_cellphone = models.CharField(max_length=15, null=True)
    contact_email = models.CharField(max_length=254)
    creator = models.ForeignKey(ContactCreator)
    contact_type = models.ForeignKey(ContactType)

    def __str__(self):
        return self.name
