"""Contact models."""
from django.conf import settings
from django.core.mail import send_mail
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
        return self.contact_email


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


def update_contact(sender, instance, **kwargs):
    creator, creating = ContactCreator.objects.get_or_create(contact_email=instance.contact_email, app=App.objects.get(pk=1))
    creator.contact_name = instance.contact_name
    creator.contact_cellphone = instance.contact_cellphone
    creator.save()


def send_notification(sender, instance, **kwargs):
    send_mail(
        'New contact created',
        'A new contact has been created by a user.',
        settings.EMAIL_DEFAULT_FROM_EMAIL,
        ['toemail@yourclient.com'],
        fail_silently=False,
    )


pre_save.connect(update_contact, sender=ContactInfo)
post_save.connect(send_notification, sender=ContactInfo)
