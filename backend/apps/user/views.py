from apps.user.serializers import UserDetailSerializer
from apps.user.services import UserDetailService
from apps.user.validate_serializers import UserIdSerializer
from rest_framework.generics import RetrieveAPIView
from rest_framework.response import Response


class UserDetailView(RetrieveAPIView):

    def __get_user_id(self):
        """
        url parameter로 부터 유저 id 가져옴.
        시리얼라이저 통해 값 검증
        """
        validator = UserIdSerializer(data=self.kwargs)
        validator.is_valid(raise_exception=True)
        user_id = validator.validated_data['user_id']
        return user_id

    def get(self, request, *args, **kwargs):
        """
        유저 상세 정보 조회
        """
        user_id = self.__get_user_id()
        target_user = UserDetailService(user_id=user_id).get_contact_detail_user()
        serialized_data = UserDetailSerializer(target_user).data
        return Response(serialized_data)
