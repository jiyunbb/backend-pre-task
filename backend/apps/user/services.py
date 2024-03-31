from apps.user.models import User, UserLabelMap
from django.db.models import Prefetch
from rest_framework.exceptions import NotFound


class UserDetailService:
    """
    유저 상세 조회 서비스
    """

    def __init__(self, user_id):
        self.user_id = user_id

    def get_contact_detail_user(self):
        target_user = User.objects.filter(pk=self.user_id).prefetch_related(
            Prefetch(
                lookup='user_label_maps',
                queryset=UserLabelMap.objects.select_related('label').all(),
                to_attr='labels'
            )
        ).first()

        if not target_user:
            raise NotFound(detail='존재하지 않는 유저입니다.')

        return target_user
