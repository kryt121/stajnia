from django.db import models
from django.urls import reverse
from django.utils import timezone

# Create your models here.

class Vehicle(models.Model):

	nazwa = models.CharField(max_length=255, verbose_name="Nazwa pojazdu")
	nr_rej = models.CharField(max_length=10, verbose_name="Numer rejestracyjny")
	SAMOCHOD_OSOBOWY='O'
	MOTOCYKL='M'
	TYPE_CHOICES = [
		(SAMOCHOD_OSOBOWY, 'Samochód osobowy'),
		(MOTOCYKL, 'Motocykl')

		]
	typ_pojazdu=models.CharField("Typ pojazdu",
		max_length=2,
		choices= TYPE_CHOICES,
		default=SAMOCHOD_OSOBOWY
		)

	uwagi = models.TextField(verbose_name="Uwagi")
	rok_produkcji = models.PositiveIntegerField(blank=False, default="1965", verbose_name="Rok produkcji")
	przebieg = models.PositiveIntegerField(blank=False, default="1", verbose_name="Przebieg [km]")
	przeglad_techniczny = models.DateField(blank=False, default="1965-01-01", verbose_name="Przegląd techniczny do")
	ubezpieczenie =  models.DateField(blank=False, default="1965-01-01", verbose_name="Ubezpieczenie do")
	wymiana_oleju =  models.DateField(blank=False, default="1965-01-01", verbose_name="Wymiana oleju do")

	class Meta():
		verbose_name = "Pojazd"
		verbose_name_plural = "Pojazdy"

	def __str__(self):
		return (self.nazwa + " / " +self.nr_rej )

	def get_absolute_url(self):
		return reverse('vehicle-detail', args=[str(self.id)])


class Action(models.Model):

	vehicle = models.ForeignKey(Vehicle, on_delete=models.PROTECT, verbose_name="Pojazd" )
	nazwa = models.CharField(max_length=255, verbose_name="Nazwa czynności")

	data_wykonania = models.DateField(
		default=timezone.now)
	przebieg = models.PositiveIntegerField(blank=False, default="1", verbose_name="Przebieg [km]")

	koszt = models.PositiveIntegerField(blank=False, default="1", verbose_name="Koszt [PLN]")
	uwagi = models.TextField(verbose_name="Uwagi")

	class Meta():
		verbose_name = "Czynność"
		verbose_name_plural = "Czynności"

	def __str__(self):
		return (self.nazwa + " / " + str(self.vehicle)+ "/" + str(self.data_wykonania) )

	def get_absolute_url(self):
		return reverse('action-detail', args=[str(self.id)])

	def save(self):
		v = Vehicle.objects.get(id=self.vehicle.id)
		if (self.przebieg > v.przebieg):
			v.przebieg = self.przebieg
			v.save()
		super(Action, self).save()
