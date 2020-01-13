from django.db import models
from crum import get_current_user

# Create your models here.
class Status(models.Model):
	name		=	models.CharField(max_length = 32)
	description	=	models.TextField(blank = True)
	created_at	=	models.DateTimeField(auto_now_add=True)
	updated_at	=	models.DateTimeField(auto_now = True)
	created_by	=	models.ForeignKey('auth.User', blank=True, null=True, default=None, on_delete=models.CASCADE, related_name='created_by')
	updated_by	=	models.ForeignKey('auth.User', blank=True, null=True, default=None, on_delete=models.CASCADE, related_name='updated_by')

	def save(self, *args, **kwargs):
		user	=	get_current_user()
		if user and not user.pk:
			user	=	None
		if not self.pk:
			self.created_by	=	user
		self.updated_by	=	user
		super(Status, self).save(*args, **kwargs)