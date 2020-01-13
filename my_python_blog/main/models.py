from django.db import models
from crum import get_current_user

# Create your models here.
class Status(models.Model):
	name		=	models.CharField(max_length = 32)
	description	=	models.TextField(blank = True)
	created_at	=	models.DateTimeField(auto_now_add=True)
	updated_at	=	models.DateTimeField(auto_now = True)
	created_by	=	models.CharField(max_length = 32)
	updated_by	=	models.CharField(max_length = 32)

	def save(self, *args, **kwargs):
		user	=	get_current_user()
		if user and not user.pk:
			user	=	None
		if not self.pk:
			self.created_by	=	user.pk
			self.updated_by	=	user.pk
			super(Status, self).save(*args, **kwargs)