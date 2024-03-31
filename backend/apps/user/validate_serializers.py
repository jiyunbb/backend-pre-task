from rest_framework import serializers


class UserIdSerializer(serializers.Serializer):
    """
    유저 아이디 검증
    """
    user_id = serializers.IntegerField(min_value=1)


class UserRequestDataSerializer(serializers.Serializer):
    """
    유저 입력 요청 데이터 검증
    """
    profile_url = serializers.CharField(allow_null=True, max_length=100, required=False)
    name = serializers.CharField(max_length=30)
    email = serializers.EmailField(max_length=50)
    tel = serializers.CharField(max_length=30)
    company = serializers.CharField(max_length=40, allow_null=True, required=False)
    position = serializers.CharField(max_length=10, allow_null=True, required=False)
    memo = serializers.CharField(max_length=30, allow_null=True, required=False)
    labels = serializers.ListField(child=serializers.IntegerField(), required=False)
    default_address = serializers.CharField(required=False, allow_null=True)
    detail_address = serializers.CharField(required=False, allow_null=True)
    zipcode = serializers.IntegerField(required=False, allow_null=True)
    birth = serializers.DateField(required=False, allow_null=True)
    website = serializers.CharField(required=False, allow_null=True)
