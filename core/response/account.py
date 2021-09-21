from rest_framework import status
from rest_framework import exceptions
from rest_framework.response import Response


class AlreadyExistEmail(Response):
    def __init__(self, message):
        super().__init__(data={
            'status': status.HTTP_400_BAD_REQUEST,
            'message': message
        })
