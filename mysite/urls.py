from django.conf.urls import url

from .view import (
    register,
    album
)

urlpatterns = [

    # register
    url(r"register$", register.AccountRegisterView.as_view()),  # POST: 계정생성

    # Albums
    url(r"album$", album.AlbumView.as_view())  # GET: 목록조회

]
