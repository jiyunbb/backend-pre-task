from apps.contact.serializers import ContactUserSerializer
from apps.contact.services import ContactUserListService, ContactUserCreateService
from apps.contact.validate_serializers import ContactIdSerializer, SortPageQueryParamSerializer
from apps.user.validate_serializers import UserIdSerializer, UserRequestDataSerializer
from rest_framework import status
from rest_framework.generics import ListCreateAPIView
from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response


class ContactUserListView(ListCreateAPIView):
    pagination_class = PageNumberPagination

    def __get_user_id(self):
        """
        header로 부터 가져온 유저 id 값 검증.
        """
        user_id: int = int(self.request.META.get('HTTP_USER_ID', 0))
        validator = UserIdSerializer(data={'user_id': user_id})
        validator.is_valid(raise_exception=True)
        user_id: int = validator.validated_data['user_id']
        return user_id

    def __get_contact_id(self):
        """
        url parameter로 부터 가져온 주소록 id 값 검증.
        """
        validator = ContactIdSerializer(data=self.kwargs)
        validator.is_valid(raise_exception=True)
        contact_id: int = validator.validated_data['contact_id']
        return contact_id

    def __get_query_params(self):
        """
        쿼리 파라미터로 부터 가져온 정렬과 페이지내이션 값 검증.
        """
        validator = SortPageQueryParamSerializer(data=self.request.query_params)
        validator.is_valid(raise_exception=True)
        sort_by = validator.validated_data.get('sort_by')
        sort_order = validator.validated_data.get('sort_order')
        page_size = validator.validated_data['page_size']
        return sort_by, sort_order, page_size

    def get(self, request, *args, **kwargs):
        """
        유저가 가지고 있는 주소록 내 유저 목록 조회
        """
        user_id: int = self.__get_user_id()
        contact_id = self.__get_contact_id()
        sort_by, sort_order, page_size = self.__get_query_params()

        # 페이지내이션 사이즈 지정
        self.pagination_class.page_size = page_size

        contact_users = ContactUserListService(
            user_id=user_id, contact_id=contact_id, sort_by=sort_by, sort_order=sort_order
        ).get_contact_users()
        page = self.paginate_queryset(contact_users)
        serialized_data = ContactUserSerializer(page, many=True).data
        return self.get_paginated_response(serialized_data)

    def post(self, request, *args, **kwargs):
        """
        주소록 유저 등록
        """
        user_id: int = self.__get_user_id()
        contact_id = self.__get_contact_id()

        validator = UserRequestDataSerializer(data=request.data)
        validator.is_valid(raise_exception=True)

        ContactUserCreateService(
            user_id=user_id, contact_id=contact_id, request_data=validator.validated_data
        ).crate_user()

        return Response(status=status.HTTP_201_CREATED)
