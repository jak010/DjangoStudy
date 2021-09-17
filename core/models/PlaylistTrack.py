from django.db import models


class PlaylistTrack(models.Model):
    playlistid = models.AutoField(db_column='PlaylistId')  # Field name made lowercase.
    trackid = models.IntegerField(db_column='TrackId')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'playlist_track'
