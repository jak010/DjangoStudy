from django.conf.urls import url
from .view import (
    register,
    album
)

urlpatterns = [

    # register
    url(r"account", register.AccountRegisterView.as_view(), name='register'),  # POST: 계정생성

    # Albums
    url(r"album$", album.AlbumView.as_view())  # GET: 목록조회

]

