from __future__ import unicode_literals

from django.db import models

class Dojos(models.Model):
	name = models.CharField(max_length = 255)
	city = models.CharField(max_length = 255)
	state = models.CharField(max_length = 255)
	created_at = models.DateTimeField(auto_now_add = True)
	updated_at = models.DateTimeField(auto_now = True)
	def __repr__(self):
		return "<Dojo: {} {} {} {} {}>".format(self.name, "|", self.city, "|",self.state)

class Ninjas(models.Model):
	dojo = models.ForeignKey(Dojos, related_name="ninjas")
	first_name = models.CharField(max_length = 255)
	last_name = models.CharField(max_length = 255)
	created_at = models.DateTimeField(auto_now_add = True)
	updated_at = models.DateTimeField(auto_now = True)
	def __repr__(self):
		return "<Ninja: {} {}>".format(self.first_name, self.last_name)

