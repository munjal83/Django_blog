from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Topic(models.Model):
	"""A Topic the user will write a blog post about"""
	text = models.CharField(max_length=200)
	date_added = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		"""Return a string representation of the model."""
		return self.text

class BlogPost(models.Model):
	"""Specific blog post about a topic"""
	topic = models.ForeignKey(Topic)
	title = models.CharField(max_length=160)
	text = models.TextField()
	date_added = models.DateTimeField(auto_now_add=True)

	class Meta:
		verbose_name_plural = 'blogposts'

	def __str__(self):
		"""Return a string representation of the model."""
		return self.title