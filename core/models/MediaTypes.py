from django.db import models


class MediaTypes(models.Model):
    mediatypeid = models.AutoField(db_column='MediaTypeId', primary_key=True)  # Field name made lowercase.
    name = models.TextField(db_column='Name', blank=True,
                            null=True)  # Field name made lowercase. This field type is a guess.

    class Meta:
        managed = False
        db_table = 'media_types'
