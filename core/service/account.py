from __future__ import annotations
from functools import cached_property

from django.core.paginator import Paginator

from rest_framework import serializers
from django_filters import rest_framework as filters

from ..models.Account import AccountModel


class AccountFilter(filters.FilterSet):
    nickname = filters.CharFilter(field_name='nickname', lookup_expr='exact')

    class Meta:
        model = AccountModel
        fields = ('nickname', 'email',)


class AccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = AccountModel
        fields = ('id', 'nickname', 'email', 'last_login')
        ordering = ('id',)


class AccountService(object):

    def __init__(self, request=None):
        self.request = request

        self.model = AccountModel
        self.serializer = AccountSerializer

    @cached_property
    def query_set(self):
        return self.model.objects.all()

    def list(self, page_number=None, page_size=None):
        """ 목록조회 """
        # TODO :  정렬(정렬키에 대해 동적으로 동작하게끔 구현 필요)

        account = AccountFilter(self.request.GET, queryset=self.query_set)
        account.is_valid()

        # page paramater 가 둘 중 한라도 없으면 전체 목록조회
        if not all([page_size, page_number]):
            qs_filter = account.filter_queryset(queryset=account.queryset).values()

            return self.serializer(
                qs_filter,
                many=True
            ).data

        # paginator 적용
        paginator = Paginator(
            account.filter_queryset(account.queryset),
            page_size
        ).page(page_number).object_list

        return self.serializer(paginator, many=True).data

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
