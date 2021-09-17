from django.core.validators import validate_email

from core.serializer.accountserialize import AccountSerializer

from rest_framework.views import APIView
from rest_framework.response import Response


class AccountRegisterView(APIView):

    def post(self, request, format=None):
        serializer = AccountSerializer(data=request.POST)
        print(serializer.is_valid())

        return Response(200)
