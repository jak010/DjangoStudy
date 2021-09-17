from django.db import models


class Employees(models.Model):
    employeeid = models.AutoField(db_column='EmployeeId', primary_key=True)  # Field name made lowercase.
    lastname = models.TextField(db_column='LastName')  # Field name made lowercase. This field type is a guess.
    firstname = models.TextField(db_column='FirstName')  # Field name made lowercase. This field type is a guess.
    title = models.TextField(db_column='Title', blank=True,
                             null=True)  # Field name made lowercase. This field type is a guess.
    reportsto = models.IntegerField(db_column='ReportsTo', blank=True, null=True)  # Field name made lowercase.
    birthdate = models.DateTimeField(db_column='BirthDate', blank=True, null=True)  # Field name made lowercase.
    hiredate = models.DateTimeField(db_column='HireDate', blank=True, null=True)  # Field name made lowercase.sd
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
    email = models.TextField(db_column='Email', blank=True,
                             null=True)  # Field name made lowercase. This field type is a guess.

    class Meta:
        managed = False
        db_table = 'employees'
