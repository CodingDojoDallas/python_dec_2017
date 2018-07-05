from __future__ import unicode_literals

from django.db import models

class User(models.Model):
	first_name = models.CharField(max_length=255)
	last_name = models.CharField(max_length=255)
	email = models.CharField(max_length=255)
	created_at = models.DateTimeField(auto_now_add = True)
	updated_at = models.DateTimeField(auto_now = True)
	def __repr__(self):
		return"<User: {} {}>".format(self.first_name, self.last_name)

class Book(models.Model):
	name = models.CharField(max_length = 255)
	desc = models.TextField(default = "")
	created_at = models.DateTimeField(auto_now_add = True)
	updated_at = models.DateTimeField(auto_now = True)
	uploader = models.ForeignKey(User, related_name="uploaded_books", default = 1)
	liked_by = models.ManyToManyField(User, related_name = "liked_books", default = 1)
	def __repr__(self):
		return "<Book: {} {}>".format(self.name, self.desc)
	def __repr__(liked_by):
		return "Books: {} {}>".format(self.first_name, self.last_name)

class Author(models.Model):
	first_name = models.CharField(max_length = 255)
	last_name = models.CharField(max_length = 255)
	email = models.CharField(max_length = 255)
	notes = models.TextField(default = "")
	created_at = models.DateTimeField(auto_now_add = True)
	updated_at = models.DateTimeField(auto_now = True)
	books = models.ManyToManyField(Book, related_name = "authors")
	def __repr__(self):
		return "<Author: {} {} >".format(self.first_name, self.last_name, self.email, self.notes)


