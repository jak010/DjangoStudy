from django.conf.urls import url
from .view import (
    account,
    album
)

urlpatterns = [

    # register
    url(r"account$", account.AccountView.as_view()),  # POST: 계정생성

    # Albums
    url(r"album$", album.AlbumView.as_view())  # GET: 목록조회

]

