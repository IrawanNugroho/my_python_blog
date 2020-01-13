from django.db import models

# Create your models here.
class Status(models.Model):
	name		=	models.CharField(max_length = 32)
	description	=	models.TextField(blank = True)
	created_at	=	models.DateTimeField(auto_now_add=True)
	updated_at	=	models.DateTimeField(auto_now = True)
	created_by	=	models.CharField(max_length = 32)
	updated_by	=	models.CharField(max_length = 32)