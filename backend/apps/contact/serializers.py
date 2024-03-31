from apps.user.serializers import BaseUserSerializer
from rest_framework import serializers


class ContactUserSerializer(BaseUserSerializer):
    company_info = serializers.CharField()

    class Meta(BaseUserSerializer.Meta):
        fields = BaseUserSerializer.Meta.fields + ('company_info',)
