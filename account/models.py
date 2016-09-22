from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User
from django.utils.encoding import python_2_unicode_compatible

# Create your models here.
@python_2_unicode_compatible
class Course(models.Model):
	owner = models.CharField(max_length= 20)
	title = models.CharField(max_length = 50)
	code = models.CharField(max_length = 7)

	def __str__(self):
		return self.title

class CourseDetail(models.Model):
	coursetitle = models.CharField(max_length = 50)
	coursecode = models.CharField(max_length = 7)


