from django.db import models
from crum import get_current_user
from tinymce.models import HTMLField


# Create your models here.
class Status(models.Model):
	name		=	models.CharField(max_length=32)
	description	=	models.TextField(blank=True)
	active		=	models.BooleanField(default=True)
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
	
	def __str__(self):
		return self.name


class Tag(models.Model):
	name		=	models.CharField(max_length=32)
	description	=	models.TextField(blank=True)
	slug		=	models.SlugField(max_length=128)
	active		=	models.BooleanField(default=True)
	created_at	=	models.DateTimeField(auto_now_add=True)
	created_by	=	models.ForeignKey('auth.User', blank=True, null=True, default=None, on_delete=models.CASCADE, related_name='tag_created_by')
	updated_at	=	models.DateTimeField(auto_now=True)
	updated_by	=	models.ForeignKey('auth.User', blank=True, null=True, default=None, on_delete=models.CASCADE, related_name='tag_updated_by')

	def save(self, *args, **kwargs):
		user	=	get_current_user()
		if user and not user.pk:
			user	=	None
		if not self.pk:
			self.created_by	=	user
		self.updated_by	=	user
		super(Tag, self).save(*args, **kwargs)
	
	def __str__(self):
		return self.name



class ArticleImage(models.Model):
	title		=	models.CharField(max_length=256)
	description	=	models.TextField(blank=True)
	author		=	models.CharField(max_length=32)
	image		=	models.ImageField(upload_to="product-images")
	thumbnail	=	models.ImageField(upload_to="product-thumbnails", null=True)
	active		=	models.BooleanField(default=True)
	created_at	=	models.DateTimeField(auto_now_add=True)
	created_by	=	models.ForeignKey('auth.User', blank=True, null=True, default=None, on_delete=models.CASCADE, related_name='image_created_by')
	updated_at	=	models.DateTimeField(auto_now=True)
	updated_by	=	models.ForeignKey('auth.User', blank=True, null=True, default=None, on_delete=models.CASCADE, related_name='image_updated_by')

	def save(self, *args, **kwargs):
		user	=	get_current_user()
		if user and not user.pk:
			user	=	None
		if not self.pk:
			self.created_by	=	user
		self.updated_by	=	user
		super(ArticleImage, self).save(*args, **kwargs)


class Article(models.Model):
	title		=	models.CharField(max_length=256)	
	content 	=	HTMLField()
	excerpt		=	models.CharField(max_length=512)
	author 		=	models.CharField(max_length=32)
	slug 		=	models.SlugField(max_length=128)
	active		=	models.BooleanField(default=True)
	status 		=	models.ForeignKey(Status, on_delete=models.CASCADE)
	tags 		=	models.ManyToManyField(Tag, blank=True)	
	created_at	=	models.DateTimeField(auto_now_add=True)
	created_by	=	models.ForeignKey('auth.User', blank=True, null=True, default=None, on_delete=models.CASCADE, related_name='article_created_by')
	updated_at	=	models.DateTimeField(auto_now=True)
	updated_by	=	models.ForeignKey('auth.User', blank=True, null=True, default=None, on_delete=models.CASCADE, related_name='article_updated_by')

	def save(self, *args, **kwargs):
		user	=	get_current_user()
		if user and not user.pk:
			user	=	None
		if not self.pk:
			self.created_by	=	user
		self.updated_by	=	user
		super(Article, self).save(*args, **kwargs)