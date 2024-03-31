from apps.contact.models import Contact, ContactUserMap
from apps.user.models import User, UserLabelMap
from django.db import transaction
from django.db.models import Prefetch
from rest_framework.exceptions import NotFound, PermissionDenied


class ContactUserListService:
    """
    유저별 주소록 내 유저 목록 조회 서비스
    """

    def __init__(self, user_id, contact_id, sort_by, sort_order):
        self.user_id = self.__validate_user(user_id)
        self.contact_id = self.__validate_contact_by_user(contact_id)
        self.sort_by = sort_by
        self.sort_order = sort_order

    def __validate_user(self, user_id):
        user = User.objects.filter(pk=user_id).exists()
        if not user:
            raise NotFound(detail='존재하지 않는 유저입니다.')

        return user_id

    def __validate_contact_by_user(self, contact_id):
        contact = Contact.objects.filter(pk=contact_id, user_id=self.user_id).exists()
        if not contact:
            # 유저에 연결되어 있지 않은 주소록을 요청하는 경우 403 오류.
            raise PermissionDenied(detail='잘못된 접근입니다.')

        return contact_id

    def __get_order_type(self):
        if not self.sort_by or not self.sort_order:
            return None

        sort_order_type = '-' if self.sort_order == User.SortOrderType.DESC else ''
        return f'{sort_order_type}{self.sort_by}'

    def get_contact_users(self):
        contact_users = User.objects.filter(contact_user_maps__contact__user_id=self.user_id).prefetch_related(
            Prefetch(
                lookup='user_label_maps',
                queryset=UserLabelMap.objects.select_related('label'),
                to_attr='labels'
            )
        )
        sort_order_type = self.__get_order_type()
        if sort_order_type:
            contact_users = contact_users.order_by(sort_order_type)

        return contact_users


class ContactUserCreateService:
    """
    유저 등록 서비스
    """

    def __init__(self, user_id, contact_id, request_data):
        self.user_id = user_id
        self.contact_id = self.__get_contact_id_by_user(contact_id)
        self.request_data = request_data

    def __get_contact_id_by_user(self, contact_id):
        contact = Contact.objects.filter(pk=contact_id, user_id=self.user_id).first()
        if not contact:
            # 유저에 연결되어 있지 않은 주소록을 요청하는 경우 403 오류.
            raise PermissionDenied(detail='잘못된 접근입니다.')

        return contact_id

    @transaction.atomic
    def crate_user(self):
        # 주소록에 등록할 유저 입력
        user: User = User.objects.create(
            profile_url=self.request_data.get('profile_url'),
            name=self.request_data['name'],
            email=self.request_data['email'],
            tel=self.request_data['tel'],
            company=self.request_data.get('company'),
            position=self.request_data.get('position'),
            memo=self.request_data.get('memo'),
            default_address=self.request_data.get('default_address'),
            detail_address=self.request_data.get('detail_address'),
            zipcode=self.request_data.get('zipcode'),
            birth=self.request_data.get('birth'),
            website=self.request_data.get('website')
        )

        # 유저와 라벨 연결
        if self.request_data.get('labels'):
            user_label_maps = [UserLabelMap(user_id=user.pk, label_id=label) for label in
                               self.request_data.get('labels')]
            UserLabelMap.objects.bulk_create(user_label_maps)

        # 유저와 유저가 담겨질 주소록 연결
        ContactUserMap.objects.create(contact_id=self.contact_id, user_id=user.pk)
