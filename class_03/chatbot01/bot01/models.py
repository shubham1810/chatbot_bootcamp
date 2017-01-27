from __future__ import unicode_literals

from django.db import models

# Create your models here.

class MyData(models.Model):
	name = models.CharField(max_length=100)
	institution = models.CharField(max_length=200)

	roll_no = models.IntegerField(null=True)