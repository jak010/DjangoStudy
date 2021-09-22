from rest_framework import status
from rest_framework import exceptions
from rest_framework.response import Response


# RestFrame Work, Exception

class Validation(Response):
    """ Raise Exception """

    def __init__(self, message):
        super().__init__(
            status=status.HTTP_400_BAD_REQUEST,
            data=message,
        )


# Custom, Exception

class Created(Response):
    """ Status, 201 """

    def __init__(self):
        super().__init__(
            status=status.HTTP_201_CREATED,
            data={
                "message": "The Resource was created successfully"
            }
        )


class CreateFail(Response):
    """ Bad Request """

    # TODO : 메세지 구체적으로 정하기
    def __init__(self):
        super().__init__(
            status=status.HTTP_400_BAD_REQUEST,
            data={
                'message': 'CreateFail'
            }
        )
