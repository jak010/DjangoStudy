from django.db import models

from rest_framework import serializers


class AlbumsModel(models.Model):
    albumid = models.AutoField(db_column='AlbumId', primary_key=True)  # Field name made lowercase.
    title = models.TextField(db_column='Title')  # Field name made lowercase. This field type is a guess.
    artistid = models.IntegerField(db_column='ArtistId')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'albums'


class AlbumsSerializer(serializers.ModelSerializer):
    class Meta:
        model = AlbumsModel
        fields = '__all__'
