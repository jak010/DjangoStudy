from drf_yasg import openapi
from rest_framework import status


class REQUEST:
    class GET:
        nickname = openapi.Parameter(
            'nickname',
            openapi.IN_QUERY,
            required=True,
            description="회원 nickname",
            type=openapi.TYPE_NUMBER
        )
        email = openapi.Parameter(
            'email',
            openapi.IN_QUERY,
            required=True,
            description="회원 nickname",
            type=openapi.TYPE_NUMBER
        )
        last_login = openapi.Parameter(
            'last_login',
            openapi.IN_QUERY,
            required=True,
            description="회원 nickname",
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
                    'application/json': {
                        'nickname': "USER_NICKNAME",
                        "email": "test@test.com",
                        "last_login": 0
                    }
                }
            )

    class POST:
        class NORMAL:
            STATUS = status.HTTP_200_OK
            MESSAGE = openapi.Response(
                description="OK",
                examples={
                    'application/json': {
                        "message": "The item was created successfully"
                    }
                }
            )

        class Validation:
            STATUS = status.HTTP_400_BAD_REQUEST
            MESSAGE = openapi.Response(
                description="Bad Request",
                examples={
                    "application/json": {
                        "key": ["Specify Description about key"],
                    }
                },
            )
