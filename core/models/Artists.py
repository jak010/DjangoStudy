from django.db import models


class Artists(models.Model):
    artistid = models.AutoField(db_column='ArtistId', primary_key=True)  # Field name made lowercase.
    name = models.TextField(db_column='Name', blank=True,
                            null=True)  # Field name made lowercase. This field type is a guess.
    _test = models.CharField(db_column='Test', max_length=10, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'artists'
