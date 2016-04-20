from django.db import models
from django.utils import timezone


class Movie(models.Model):
	title = models.CharField(max_length=200)
	intro = models.TextField()
	rate = models.FloatField()
	published_date = models.DateField()
	clsed_date = models.DateField()

	def __str__(self):
		return self.title

class Theater(models.Model):
	movie = models.ManyToManyField(Movie)
	name = models.CharField(max_length=200)

	def __str__(self):
		return self.name

class Director(models.Model):
	movie = models.ManyToManyField(Movie)
	name = models.CharField(max_length=100)

	def __str__(self):
		return self.name

class Actor(models.Model):
	movie = models.ManyToManyField(Movie)
	name = models.CharField(max_length=100)

	def __str__(self):
		return self.name

class Review(models.Model):
	movie = models.ForeignKey(Movie, related_name='review') # 'movies.Movie'
	name = models.CharField(max_length=100)
	text = models.TextField()
	created_date = models.DateTimeField(default=timezone.now)

	def __str__(self):
		return self.text