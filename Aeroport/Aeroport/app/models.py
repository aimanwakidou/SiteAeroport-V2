# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models

class Companies(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    iata = models.CharField(db_column='IATA', unique=True, max_length=3)  # Field name made lowercase.
    name = models.CharField(db_column='Name', max_length=40)  # Field name made lowercase.
    logo = models.CharField(db_column='Logo', max_length=2083)  # Field name made lowercase.

    class Meta:
        db_table = 'companies'


class Countries(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    code = models.CharField(db_column='Code', unique=True, max_length=2)  # Field name made lowercase.
    frenchname = models.CharField(db_column='FrenchName', max_length=100)  # Field name made lowercase.
    englishname = models.CharField(db_column='EnglishName', max_length=100)  # Field name made lowercase.

    class Meta:
        db_table = 'countries'

class Airport(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    iata = models.CharField(db_column='IATA', unique=True, max_length=3)  # Field name made lowercase.
    name = models.CharField(db_column='Name', max_length=40)  # Field name made lowercase.
    fullname = models.CharField(db_column='FullName', max_length=100)  # Field name made lowercase.
    country = models.ForeignKey(Countries, models.DO_NOTHING, db_column='Id_Countries')  # Field name made lowercase.

    class Meta:
        db_table = 'airport'

class Flights(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    flight_number = models.IntegerField(db_column='Flight_number')  # Field name made lowercase.
    status = models.CharField(db_column='Status', max_length=9, blank=True, null=True)  # Field name made lowercase.
    day = models.CharField(db_column='Day', max_length=9)  # Field name made lowercase.
    flight_time = models.TimeField(db_column='Flight_time')  # Field name made lowercase.
    flight_type = models.CharField(db_column='Flight_type', max_length=9)  # Field name made lowercase.
    departure = models.ForeignKey(Airport, models.DO_NOTHING, db_column='Id_From',related_name="Departure")  # Field name made lowercase.
    arrival = models.ForeignKey(Airport, models.DO_NOTHING, db_column='Id_To',related_name="Arrival")  # Field name made lowercase.
    company = models.ForeignKey(Companies, models.DO_NOTHING, db_column='Id_Companies')  # Field name made lowercase.

    class Meta:
        db_table = 'flights'

class DelayedFlights(models.Model):
    flight = models.ForeignKey(Flights, models.DO_NOTHING, db_column='Id_Flight', primary_key=True)  # Field name made lowercase.
    deleyed_time = models.DateTimeField(db_column='Deleyed_Time')  # Field name made lowercase.

    class Meta:
        db_table = 'delayed_flights'

class Luggage(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    reference = models.CharField(db_column='Reference', unique=True, max_length=255)  # Field name made lowercase.
    flight = models.ForeignKey(Flights, models.DO_NOTHING, db_column='Id_Flight')  # Field name made lowercase.

    class Meta:
        db_table = 'luggage'


class User(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    first_name = models.CharField(db_column='First_Name', max_length=60, blank=True, null=True)  # Field name made lowercase.
    last_name = models.CharField(db_column='Last_Name', max_length=100, blank=True, null=True)  # Field name made lowercase.
    email = models.CharField(db_column='Email', unique=True, max_length=150, blank=True, null=True)  # Field name made lowercase.
    phone = models.CharField(db_column='Phone', max_length=11, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        db_table = 'user'

class Alerts(models.Model):
    id_user = models.ForeignKey(User, models.DO_NOTHING, db_column='Id_User')  # Field name made lowercase.
    id_flight = models.ForeignKey(Flights, models.DO_NOTHING, db_column='Id_Flight')  # Field name made lowercase.

    class Meta:
        db_table = 'alerts'
        unique_together = ('id_user', 'id_flight')


class Weather(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    local_name = models.CharField(db_column='Local_Name', max_length=50)  # Field name made lowercase.
    icon_url = models.CharField(db_column='Icon_Url', max_length=2083, blank=True, null=True)  # Field name made lowercase.
    temperature = models.IntegerField(db_column='Temperature')  # Field name made lowercase.
    wind_speed = models.IntegerField(db_column='Wind_Speed', blank=True, null=True)  # Field name made lowercase.
    time_description = models.TextField(db_column='Time_Description', blank=True, null=True)  # Field name made lowercase.
    airport = models.ForeignKey(Airport, models.DO_NOTHING, db_column='Id_Airport', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        db_table = 'weather'
