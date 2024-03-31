from apps.user.models import User
from django.db import models


class Contact(models.Model):
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING, db_column='user_id', related_name='contacts')
    name = models.CharField(max_length=20)

    class Meta:
        managed = False
        verbose_name = '주소록 테이블'
        db_table = 'contact'


class ContactUserMap(models.Model):
    contact = models.ForeignKey(Contact, on_delete=models.DO_NOTHING, db_column='contact_id',
                                related_name='contact_user_maps')
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING, db_column='user_id', related_name='contact_user_maps')

    class Meta:
        managed = False
        verbose_name = '주소록에 연결된 유저 매핑 테이블'
        db_table = 'contact_user_map'
