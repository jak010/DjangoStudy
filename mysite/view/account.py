from rest_framework.views import APIView
from rest_framework import mixins, generics
from rest_framework import exceptions
from rest_framework.response import Response

from drf_yasg.utils import swagger_auto_schema

from core.service import account
from core.document import account as _doc
from core import response


class AccountView(
    generics.GenericAPIView
):
    serializer_class = account.AccountSerializer
    queryset = account.AccountModel.objects.all()
    filter_class = account.AccountFilterSet

    @swagger_auto_schema(
        operation_id='유저 데이터 조회',
        operation_description="유저 데이터 조회",

        manual_parameters=[
            _doc.REQUEST.GET.email,
            _doc.REQUEST.GET.nickname,
            _doc.REQUEST.GET.last_login_from,
            _doc.REQUEST.GET.last_login_to,
        ],

        responses={
            _doc.RESPONSE.GET.NORMAL.STATUS: _doc.RESPONSE.GET.NORMAL.MESSAGE
        }
    )
    def get(self, request, *args, **kwargs):
        """ 유저 목록 조회 """

        data = account.AccountService(request=request)

        return Response(data=data.list())

    @swagger_auto_schema(
        operation_id="유저 생성",
        operation_description=
        """
        유저 생성, email, passsword, nickname을 받아서 생성        
        """,

        request_body=_doc.REQUEST.POST.body,

        responses={
            _doc.RESPONSE.POST.NORMAL.STATUS: _doc.RESPONSE.POST.NORMAL.MESSAGE,
            _doc.RESPONSE.POST.Validation.STATUS: _doc.RESPONSE.POST.Validation.MESSAGE
        }

    )
    def post(self, request):
        """ 유저 생성 """
        try:
            service = account.AccountService(request=request.POST)
        except exceptions.ValidationError as err:
            return response.Validation(message=err.detail)

        if not service.create():
            return response.CreateFail()

        return response.Created()
