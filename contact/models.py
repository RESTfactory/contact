"""Contact models."""
from django.db import models
from django.db.models.signals import (
    pre_save,
    post_save
)
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
    description = models.CharField(max_length=100, blank=True, null=True)
    organizational_unit = models.ForeignKey(OrganizationalUnit)

    def __str__(self):
        return self.name


class ContactInfo(models.Model):
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    contact_name = models.CharField(max_length=100, null=True)
    contact_cellphone = models.CharField(max_length=15, null=True)
    contact_email = models.CharField(max_length=254)
    creator = models.ForeignKey(ContactCreator, blank=True, null=True)
    contact_type = models.ForeignKey(ContactType)

    def __str__(self):
        return str(self.contact_email)+" - "+str(self.created_at)


def creating_contact(sender, **kwargs):
    # Do something
    print("#"*30)
    print("creating_contact")
    print("#"*30)
    pass


def contact_created(sender, **kwargs):
    # Do something
    print("#"*30)
    print("contact_created")
    print("#"*30)
    pass


pre_save.connect(creating_contact, sender=ContactInfo)
post_save.connect(contact_created, sender=ContactInfo)
