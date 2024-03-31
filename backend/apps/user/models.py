from django.db import models
from django.db.models import TextChoices


class User(models.Model):
    profile_url = models.CharField(max_length=100, null=True)
    name = models.CharField(max_length=30)
    email = models.EmailField(unique=True, max_length=50)
    tel = models.CharField(unique=True, max_length=10)
    company = models.CharField(max_length=40, null=True)
    position = models.CharField(max_length=10, null=True)
    memo = models.CharField(max_length=30, null=True)
    default_address = models.CharField(max_length=100, null=True)
    detail_address = models.CharField(max_length=100, null=True)
    zipcode = models.CharField(max_length=6, null=True)
    birth = models.DateField(null=True)
    website = models.CharField(max_length=300, null=True)

    def full_address(self):
        if not (self.zipcode or self.default_address or self.detail_address):
            return None

        return f'{self.zipcode}, {self.default_address} {self.detail_address}'

    def company_info(self):
        if not self.company:
            return None

        position = self.position if self.position else '-'
        return f'{self.company} ({position})'

    class SortByType(TextChoices):
        NAME = 'name', '이름'
        EMAIL = 'email', '이메일'
        TEL = 'tel', '전화번호'

    class SortOrderType(TextChoices):
        ASC = 'asc', '오름차순'
        DESC = 'desc', '내림차순'

    class Meta:
        managed = False
        verbose_name = '유저 테이블'
        db_table = 'user'


class Label(models.Model):
    name = models.CharField(max_length=20)

    class Meta:
        managed = False
        verbose_name = '라벨 테이블'
        db_table = 'label'


class UserLabelMap(models.Model):
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING, db_column='user_id', related_name='user_label_maps')
    label = models.ForeignKey(Label, on_delete=models.DO_NOTHING, db_column='label_id', related_name='user_label_maps')

    class Meta:
        managed = False
        verbose_name = '유저에 연결된 라벨 매핑 테이블'
        db_table = 'user_label_map'
