from apps.user.models import Label, User
from rest_framework import serializers


class LabelSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(source='label.id')
    name = serializers.CharField(source='label.name')

    class Meta:
        model = Label
        fields = ('id', 'name',)


class BaseUserSerializer(serializers.ModelSerializer):
    profile_url = serializers.CharField()
    name = serializers.CharField()
    email = serializers.EmailField()
    tel = serializers.CharField()
    labels = LabelSerializer(many=True)

    class Meta:
        model = User
        fields = ('profile_url', 'name', 'email', 'tel', 'labels')


class UserDetailSerializer(BaseUserSerializer):
    memo = serializers.CharField()
    company = serializers.CharField()
    position = serializers.CharField()
    address = serializers.CharField(source='full_address')
    birth = serializers.DateField()
    website = serializers.CharField()

    class Meta(BaseUserSerializer.Meta):
        fields = BaseUserSerializer.Meta.fields + ('memo', 'company', 'position', 'address', 'birth', 'website')
