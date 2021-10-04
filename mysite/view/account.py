from django.utils.decorators import method_decorator
from django.core.paginator import EmptyPage, PageNotAnInteger

from rest_framework import generics
from rest_framework import exceptions
from rest_framework.response import Response

from drf_yasg.utils import swagger_auto_schema

from core.service import account
from core.document import account as _doc
from core import response


@method_decorator(name='get', decorator=swagger_auto_schema(
    operation_id='유저 데이터 조회',
    operation_description="유저 데이터 조회",

    manual_parameters=[
        _doc.REQUEST.GET.email,
        _doc.REQUEST.GET.nickname,
        _doc.REQUEST.GET.last_login_from,
        _doc.REQUEST.GET.last_login_to,
        _doc.REQUEST.GET.page_size,
        _doc.REQUEST.GET.page_number,
    ],

    responses={
        _doc.RESPONSE.GET.NORMAL.STATUS: _doc.RESPONSE.GET.NORMAL.MESSAGE
    }
))
@method_decorator(name='post', decorator=swagger_auto_schema(
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
))
class AccountView(generics.GenericAPIView):
    filter_class = account.AccountFilter

    @swagger_auto_schema(
        operation_id='유저 데이터 조회',
        operation_description="유저 데이터 조회",
        manual_parameters=[
            _doc.REQUEST.GET.email,
            _doc.REQUEST.GET.nickname,
            _doc.REQUEST.GET.last_login_from,
            _doc.REQUEST.GET.last_login_to,
            _doc.REQUEST.GET.page_size,
            _doc.REQUEST.GET.page_number,
        ],
        responses={
            _doc.RESPONSE.GET.NORMAL.STATUS: _doc.RESPONSE.GET.NORMAL.MESSAGE
        }
    )
    def get(self, request):
        """ 유저 목록 조회 """
        from appsig import signals

        signals.signal_test.send(
            sender=self.__class__.__name__
        )

        try:
            page_number = self.request.query_params.get("page_number", default=None)
            page_size = self.request.query_params.get("page_size", default=None)
        except PageNotAnInteger as err:
            return response.Validation(message={"detail": "Invalid Page."})

        try:
            data = account.AccountService(request) \
                .list(page_number=page_number, page_size=page_size)
        except EmptyPage as err:
            return response.Validation(message={"detail": "Invalid Page."})

        return Response(data=data)

    def post(self, request):
        """ 유저 생성 """
        try:
            service = account.AccountService(request=request.POST)
        except exceptions.ValidationError as err:
            return response.Validation(message=err.detail)

        if not service.create():
            return response.CreateFail()

        return response.Created()
