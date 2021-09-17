from django.db import models


class Tracks(models.Model):
    trackid = models.AutoField(db_column='TrackId', primary_key=True)  # Field name made lowercase.
    name = models.TextField(db_column='Name')  # Field name made lowercase. This field type is a guess.
    albumid = models.IntegerField(db_column='AlbumId', blank=True, null=True)  # Field name made lowercase.
    mediatypeid = models.IntegerField(db_column='MediaTypeId')  # Field name made lowercase.
    genreid = models.IntegerField(db_column='GenreId', blank=True, null=True)  # Field name made lowercase.
    composer = models.TextField(db_column='Composer', blank=True,
                                null=True)  # Field name made lowercase. This field type is a guess.
    milliseconds = models.IntegerField(db_column='Milliseconds')  # Field name made lowercase.
    bytes = models.IntegerField(db_column='Bytes', blank=True, null=True)  # Field name made lowercase.
    unitprice = models.TextField(db_column='UnitPrice')  # Field name made lowercase. This field type is a guess.

    class Meta:
        managed = False
        db_table = 'tracks'