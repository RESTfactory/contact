from rest_framework import serializers
from .models import (
    ContactCreator,
    ContactType,
    ContactInfo
)


class ContactCreatorSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContactCreator
        fields = '__all__'

class ContactTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContactType
        fields = '__all__'


class ContactInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContactInfo
        fields = '__all__'
