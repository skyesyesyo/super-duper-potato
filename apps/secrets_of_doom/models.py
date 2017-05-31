# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Secret(models.Model):
	content = models.TextField()
	user = models.ForeignKey("login_of_doom.User")
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)

class Like(models.Model):
	user = models.ForeignKey("login_of_doom.User")
	secret = models.ForeignKey("Secret")
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)