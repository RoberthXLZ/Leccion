# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models


# Create your models here.

class Tickes (models.Model):
	#Fecha de emision
	fecha_de_emision= models.DateField()
	#origen y destinio
	GUAYAQUIL='Guayaquil'	
	QUITO='Quito'
	PLAYAS ='Playas'
	MACHALA ='Machala'
	PORTOVIEJO ='Portoviejo'
	origen = (
		GUAYAQUIL,'Guayaquil',	
		QUITO,'Quito',
		PLAYAS,'Playas',
		MACHALA,'Machala',
		PORTOVIEJO,'Portoviejo',
	)


	CHONE='Chone'	
	POSORJA='Posorja'
	QUEVEDO ='Quevedo'
	MANTA ='Manta'
	CANOA ='Canoa'
	destino = (
		CHONE,'Chone',	
		POSORJA,'Posorja',
		QUEVEDO,'Quevedo',
		MANTA,'Manta',
		CANOA,'Canoa',
	)

	#precio	
	precio = models.DecimalField(max_digits = 8, decimal_places = 2)
	#adquiriente
	adquiriente = models.CharField(max_length=10)
	puesto=models.IntegerField()


