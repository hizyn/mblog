#coding=utf-8
from django.db import models
from django.utils import timezone

# Create your models here.
class Author(models.Model):
	name = models.CharField(max_length=200)
	description = models.CharField(max_length=1000)

	class Meta:
		verbose_name = '作者'
		verbose_name_plural = '作者'

	def __unicode__(self):
		return u'%s' % self.name


class Column(models.Model):
	name = models.CharField(max_length=200)
	description = models.CharField(max_length=1000)

	class Meta:
		verbose_name = '栏目'
		verbose_name_plural = '栏目'

	def __unicode__(self):
		return u'%s' % self.name


class Tag(models.Model):
	name = models.CharField(max_length=200)
	description = models.CharField(max_length=1000)

	class Meta:
		verbose_name = '标签'
		verbose_name_plural = '标签'

	def __unicode__(self):
		return u'%s' % self.name

class Post(models.Model):
	title = models.CharField(max_length=200)
	description = models.CharField(max_length=1000)
	date = models.DateTimeField(default=timezone.now())
	author = models.ForeignKey(Author)
	column = models.ForeignKey(Column)
	tag = models.ManyToManyField(Tag)
	status = models.BooleanField(default=True)
	visits = models.IntegerField(default=0)
	content = models.TextField(max_length=3000)

	class Meta:
		verbose_name = '文章'
		verbose_name_plural = '文章'

	def __unicode__(self):
		return '%s' % self.title
