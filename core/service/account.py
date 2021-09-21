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

        if self.seralizer.is_valid(raise_exception=True):
            self.valid_email = self.seralizer.validated_data.get("email")
            self.valid_password = self.seralizer.validated_data.get("password")
            self.valid_nickname = self.seralizer.validated_data.get("nickname")

    def list(self):
        pass

    def retreive(self):
        pass

    def create(self):
        """ 유저 생성하기 """

        result = AccountModel.objects.create_user(
            email=self.valid_email,
            password=self.valid_password,
            nickname=self.valid_nickname
        )

        return result
