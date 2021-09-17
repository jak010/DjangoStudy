from django.db import models


class Customers(models.Model):
    customerid = models.AutoField(db_column='CustomerId', primary_key=True)  # Field name made lowercase.
    firstname = models.TextField(db_column='FirstName')  # Field name made lowercase. This field type is a guess.
    lastname = models.TextField(db_column='LastName')  # Field name made lowercase. This field type is a guess.
    company = models.TextField(db_column='Company', blank=True,
                               null=True)  # Field name made lowercase. This field type is a guess.
    address = models.TextField(db_column='Address', blank=True,
                               null=True)  # Field name made lowercase. This field type is a guess.
    city = models.TextField(db_column='City', blank=True,
                            null=True)  # Field name made lowercase. This field type is a guess.
    state = models.TextField(db_column='State', blank=True,
                             null=True)  # Field name made lowercase. This field type is a guess.
    country = models.TextField(db_column='Country', blank=True,
                               null=True)  # Field name made lowercase. This field type is a guess.
    postalcode = models.TextField(db_column='PostalCode', blank=True,
                                  null=True)  # Field name made lowercase. This field type is a guess.
    phone = models.TextField(db_column='Phone', blank=True,
                             null=True)  # Field name made lowercase. This field type is a guess.
    fax = models.TextField(db_column='Fax', blank=True,
                           null=True)  # Field name made lowercase. This field type is a guess.
    email = models.TextField(db_column='Email')  # Field name made lowercase. This field type is a guess.
    supportrepid = models.IntegerField(db_column='SupportRepId', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'customers'
