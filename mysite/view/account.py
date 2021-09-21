from rest_framework.views import APIView
from rest_framework import status
from rest_framework import exceptions
from rest_framework.response import Response

from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema

from core.service import account
from core.document import account as _doc
from core.response import account as _response


class AccountView(APIView):

    @swagger_auto_schema(
        operation_id='^mystie/account',
        operation_description="유저 데이터 조회입니다",

        manual_parameters=[
            _doc.REQUEST.GET.email,
            _doc.REQUEST.GET.nickname,
            _doc.REQUEST.GET.last_login
        ],

        responses={
            _doc.RESPONSE.GET.NORMAL.STATUS: _doc.RESPONSE.GET.NORMAL.MESSAGE
        }
    )
    def get(self, request):
        """ 유저 목록 조회 """
        return Response({"message": "ok"})

    @swagger_auto_schema(
        operation_id="^mystie/account",
        operation_description="유저 생성",

        request_body=_doc.REQUEST.POST.body,

        responses={
            _doc.RESPONSE.POST.NORMAL.STATUS: _doc.RESPONSE.POST.NORMAL.MESSAGE,
            _doc.RESPONSE.POST.AlreadyExistEmail.STATUS: _doc.RESPONSE.POST.AlreadyExistEmail.MESSAGE
        }

    )
    def post(self, request):

        try:
            service = account.AccountService(request=request.POST)
        except exceptions.ValidationError as err:
            return _response.AlreadyExistEmail(message=err.detail.get('email'))

        if not service.create():
            return Response(status=status.HTTP_400_BAD_REQUEST)

        return Response(data={
            'email': service.valid_email,
            'name': service.valid_nickname
        })
