from apps.user.models import User
from rest_framework import serializers


class ContactIdSerializer(serializers.Serializer):
    """
    주소록 아이디 검증
    """
    contact_id = serializers.IntegerField(min_value=1)


class SortPageQueryParamSerializer(serializers.Serializer):
    """
    주소록 유저 조회시 정렬값과 페이지내이션 쿼리 파라미터 검증
    """
    page = serializers.IntegerField(min_value=1)
    page_size = serializers.IntegerField(min_value=1)
    sort_by = serializers.ChoiceField(choices=User.SortByType.choices, required=False)
    sort_order = serializers.ChoiceField(choices=User.SortOrderType.choices, required=False)
