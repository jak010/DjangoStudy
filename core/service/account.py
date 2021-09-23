from __future__ import annotations

from rest_framework import serializers
from django_filters import rest_framework as filters

from ..models.Account import AccountModel


class AccountFilterSet(filters.FilterSet):
    nickname = filters.CharFilter(field_name='nickname', lookup_expr='exact')

    class Meta:
        model = AccountModel
        fields = ('nickname', 'email')


class AccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = AccountModel
        fields = ['id', 'nickname', 'email', 'last_login', 'level']


class AccountService(object):

    def __init__(self, request=None):
        self.request = request

        self.model = AccountModel

    def list(self):
        """ 목록조회 """
        # TODO : 필터링, 정렬, 페이지네이션

        # 필터링 예제 21.09.24
        queryset = self.model.objects.all()
        account = AccountFilterSet(self.request.GET, queryset=queryset)

        if account.is_valid():
            qs_filter = account.filter_queryset(queryset=account.queryset) \
                .values('id', 'nickname', 'email', 'last_login')
            return qs_filter
        else:
            return list()

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
