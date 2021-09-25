from drf_yasg import openapi
from rest_framework import status


class REQUEST:
    class GET:
        nickname = openapi.Parameter(
            'nickname',
            openapi.IN_QUERY,
            description="acoount, nickname",
            type=openapi.TYPE_STRING
        )
        email = openapi.Parameter(
            'email',
            openapi.IN_QUERY,
            description="account, email",
            type=openapi.TYPE_STRING
        )
        last_login_from = openapi.Parameter(
            'last_login_from',
            openapi.IN_QUERY,
            description="account, last_login",
            type=openapi.TYPE_NUMBER
        )

        last_login_to = openapi.Parameter(
            'last_login_to',
            openapi.IN_QUERY,
            description="account, last_login",
            type=openapi.TYPE_NUMBER
        )

        page_size = openapi.Parameter(
            'page_size',
            openapi.IN_QUERY,
            description="account, page_size",
            type=openapi.TYPE_NUMBER
        )

        page_number = openapi.Parameter(
            'page_number',
            openapi.IN_QUERY,
            description="account, page_number",
            type=openapi.TYPE_NUMBER
        )

    class POST:
        body = openapi.Schema(
            type=openapi.TYPE_OBJECT,
            properties={
                'reg_nickname': openapi.Schema(type=openapi.TYPE_STRING, description='string'),
                'reg_email': openapi.Schema(type=openapi.TYPE_STRING, description='string'),
                'reg_password': openapi.Schema(type=openapi.TYPE_STRING, description='string')
            },
            required=['reg_nickname', 'reg_email', 'reg_password']
        )


class RESPONSE:
    class GET:
        class NORMAL:
            STATUS = status.HTTP_200_OK
            MESSAGE = openapi.Response(
                description="OK",
                examples={
                    'application/json': [{
                        'id': 'int',
                        'nickname': "string",
                        "email": "string",
                        "last_login": 0
                    }]
                }
            )

    class POST:
        class NORMAL:
            STATUS = status.HTTP_201_CREATED
            MESSAGE = openapi.Response(
                description="OK",
                examples={
                    'application/json': {
                        "message": "The Resource was created successfully"
                    }
                }
            )

        class Validation:
            STATUS = status.HTTP_400_BAD_REQUEST
            MESSAGE = openapi.Response(
                description="Bad Request",
                examples={
                    "application/json": {
                        "nickname": [
                            "account model with this nick_name already exists."
                        ],
                        "email": [
                            "account model with this email already exists."
                        ]
                    }
                },
            )
