from django.conf import settings
from django.db import models

class App(models.Model):
    name = models.CharField(max_length=30)
    # owner = models.ForeignKey(settings.AUTH_USER_MODEL)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

class OrganizationalUnitType(models.Model):
    name = models.CharField(max_length=30)
    description = models.CharField(max_length=30, blank=True)
    app = models.ForeignKey(App)
    parent = models.ForeignKey('self', blank=True, null=True, related_name='children')

    def __str__(self):
        return self.name

class OrganizationalUnit(models.Model):
    name = models.CharField(max_length=30)
    description = models.CharField(max_length=30, blank=True)
    unit_type = models.ForeignKey(OrganizationalUnitType, related_name="units")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
