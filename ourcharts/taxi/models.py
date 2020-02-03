# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Myorder(models.Model):
    order_id = models.CharField(primary_key=True, max_length=50)
    start_time = models.CharField(max_length=20)
    end_time = models.CharField(max_length=20)
    start_longitude = models.CharField(max_length=20)
    start_latitude = models.CharField(max_length=20)
    end_longitude = models.CharField(max_length=20)
    end_latitude = models.CharField(max_length=20)

    class Meta:
        managed = False
        db_table = 'myorder'


class Position(models.Model):
    driver_id = models.CharField(max_length=50)
    order_id = models.CharField(max_length=50)
    time_stamp = models.CharField(primary_key=True, max_length=20)
    longitude = models.CharField(max_length=20)
    latitude = models.CharField(max_length=20)

    class Meta:
        managed = False
        db_table = 'position'
        unique_together = (('time_stamp', 'order_id'),)


class Test(models.Model):
    id = models.CharField(max_length=30)
    time = models.CharField(max_length=30)
    number = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'test'
