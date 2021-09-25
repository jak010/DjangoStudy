from __future__ import annotations
from functools import cached_property

from django.core.paginator import Paginator

from rest_framework import serializers
from django_filters import rest_framework as filters


from ..models.Account import AccountModel


class AccountFilterSet(filters.FilterSet):
    nickname = filters.CharFilter(field_name='nickname', lookup_expr='exact')

    class Meta:
        model = AccountModel
        fields = ('nickname', 'email',)


class AccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = AccountModel
        fields = ('id', 'nickname', 'email', 'last_login')


class AccountService(object):

    def __init__(self, request=None):
        self.request = request

        self.model = AccountModel
        self.serializer = AccountSerializer


    def list(self, page_number=None, page_size=None):
        """ 목록조회 """
        # TODO : 필터링, 정렬, 페이지네이션
        queryset = self.model.objects.all() \
            .values('id', 'email', 'nickname', 'last_login').order_by('-id')

        if page_size is None:
            return list(Paginator(queryset, page_size).page(page_number))
        else:
            return queryset

#     @cached_property
#     def query_set(self):
#         return self.model.objects.all()

#     def list(self):
#         """ 목록조회 """
#         # TODO : 필터링, 정렬, 페이지네이션

#         # 필터링 예제 21.09.24
#         account = AccountFilterSet(self.request.GET, queryset=self.query_set)

#         if account.is_valid():
#             return self.serializer(
#                 account.filter_queryset(
#                     queryset=account.queryset
#                 ).values(),
#                 many=True
#             ).data
#         else:
#             return list()
# >>>>>>> main

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
