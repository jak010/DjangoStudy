from rest_framework import status
from rest_framework import exceptions
from rest_framework.response import Response


class Normal(Response):
    """ Normal """

    def __init__(self):
        super().__init__(
            status=status.HTTP_200_OK,
            data={
                "message": "The item was created successfully"
            }
        )


class Validation(Response):
    """ Raise Exception """

    def __init__(self, message):
        super().__init__(
            status=status.HTTP_400_BAD_REQUEST,
            data=message,
        )


class CreateFail(Response):
    """ Bad Request """

    # TODO : 메세지 구체적으로 정하기
    def __init__(self):
        super().__init__(
            status=status.HTTP_400_BAD_REQUEST,
            data={
                'message': '"CreateFail"'
            }
        )
