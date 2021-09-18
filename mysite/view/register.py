from django.core.validators import validate_email

from core.serializer.accountserialize import AccountSerializer

from rest_framework.views import APIView
from rest_framework.response import Response

from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema

from rest_framework import generics

from core.serializer.accountserialize import AccountSerializer


class AccountRegisterView(APIView):
    # GET
    test_param = openapi.Parameter('test', openapi.IN_QUERY,
                                   description="test manual param",
                                   type=openapi.TYPE_NUMBER)

    @swagger_auto_schema(
        operation_id='유저 목록조회',
        operation_description="유저 데이터 조회입니다",
        manual_parameters=[test_param],
        responses={200: openapi.Response('', AccountSerializer(many=True))}

    )
    def get(self, request):
        return Response({"message": "ok"})

    @swagger_auto_schema(
        operation_id='유저 생성하기',
        operation_description=
        """
            @POST, ACCOUNT는 유저 생성입니다.
        """
    )
    def post(self, request):
        serializer = AccountSerializer(data=request.POST)
        print(serializer.is_valid())

        return Response(200)
