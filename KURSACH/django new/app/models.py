"""
Definition of models.
"""

from django.db import models
from django.shortcuts import reverse

# Create your models here.
# Уже начала
#class station(models.Model):
 #   name=models.CharField(max_length=128)
 #   slug=models.SlugField(max_length=128, unique=True)
 #   type=models.CharField(max_length=128)
  #  def __str__(self):
   #     return '{}'.format(self.name)

#class Stations(models.Model):
   # name=models.CharField(max_length=128)
 #   slug=models.SlugField(max_length=128, unique=True)
 #   type=models.CharField(max_length=128)
#    point_dep = models.ManyToManyField('Departure', related_name='stations')
 #   point_arr = models.ManyToManyField('Arrival', related_name='stations')
 #   train = models.ManyToManyField('Trains', related_name='trains')
 #   def __str_(self):
 #       return '{}'.format(self.name)

#class Departure(models.Model):
 #   name=models.CharField(max_length=128)
 #   slug=models.SlugField(max_length=128, unique=True)
 #   train = models.ManyToManyField('Trains', related_name='trains')
#    point_arr = models.ManyToManyField('Arrival', related_name='stations')

#class Arrival(models.Model):
#    name=models.CharField(max_length=128)
#    slug=models.SlugField(max_length=128, unique=True)
#    train = models.ManyToManyField('Trains', related_name='trains')

#class Trains(models.Model):
    #time_dep = models.CharField(max_lenth=128)
    #time_arr= models.CharField(max_lenth=128)
    #name_train=models.CharField(max_lenth=128)
    #model =models.CharField(max_lenth=128)
   # type= models.CharField(max_lenth=128)
  # type= models.CharField(max_lenth=128)
  #  slug=models.SlugField(max_length=128, unique=True)
