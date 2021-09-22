from __future__ import annotations

from rest_framework import serializers
from ..models.Account import AccountModel


class AccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = AccountModel
        fields = '__all__'


class AccountService(object):

    def __init__(self, request=None):
        self.request = request

        self.model = AccountModel
        self.serializer = AccountSerializer

    def list(self):
        """ 목록조회 """
        # TODO : 필터링, 정렬, 페이지네이션
        queryset = self.model.objects.all().values('id', 'email', 'nickname', 'last_login')
        return list(queryset)

    def retreive(self):
        pass

    def create(self):
        """ 유저 생성 """
        serializer = self.serializer(data=self.request, partial=True)

        if serializer.is_valid(raise_exception=True):
            valid_email = serializer.validated_data.get("email")
            valid_password = serializer.validated_data.get("password")
            valid_nickname = serializer.validated_data.get("nickname")

        return AccountModel.objects.create_user(
            email=valid_email,
            password=valid_password,
            nickname=valid_nickname
        )
