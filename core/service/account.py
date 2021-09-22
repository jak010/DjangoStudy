from __future__ import annotations

from rest_framework import serializers

from ..models.Account import AccountModel


class AccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = AccountModel
        fields = '__all__'


class AccountService(object):

    def __init__(self, request):
        self.seralizer: AccountSerializer = AccountSerializer(data=request, partial=True)

    def list(self):
        pass

    def retreive(self):
        pass

    def create(self):
        """ 유저 생성하기 """
        if self.seralizer.is_valid(raise_exception=True):
            valid_email = self.seralizer.validated_data.get("email")
            valid_password = self.seralizer.validated_data.get("password")
            valid_nickname = self.seralizer.validated_data.get("nickname")

        result = AccountModel.objects.create_user(
            email=valid_email,
            password=valid_password,
            nickname=valid_nickname
        )

        return result
