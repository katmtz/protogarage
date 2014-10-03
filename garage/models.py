from django.db import models
from django.contrib.auth.models import User

class Builder(models.model):
# individual user: links to django user auth
	full_name = models.CharField(max_length=70, verbose_name="name")
	profpic = models.ImageField(null=True)
	user = models.ForeignKey(User)

	def __str__(self):
		return self.full_name

	def get_username(self):
		return self.user.id

	def get_email(self):
		return self.user.email

	def get_date_joined(self):
		return self.user.date_joined

	def get_teams(self):
		return Team.objects.filter(user=self.user)

class Team(models.Model):
# team/project: links to members, parts, documentation
	
	# basic project info: project name, members, short description
	name = models.CharField(max_length=128)
	members = models.ManyToManyField(Builder, through='Membership')
	description = models.CharField(max_length=500, null=True)
    image = models.ImageField(null=True)

	# technical info about project
	docs = models.TextField(null=True) # can have HTML, unlimited text
	parts = models.ManyToManyField(Part,null=True)

	def __str__(self):
		return self.name

class Membership(models.Model):
# defines relationship btwn Team and Builder
	builder = models.ForeignKey(Builder)
	team = models.ForeignKey(Team)
	year = models.DateField()

class Part(models.Model):
# individual part info by team
	name = models.CharField(max_length=128)
	source = models.URLField()
	count = models.IntegerField()
	cost = models.DecimalField(decimal_places=2)

	def __str__(self):
		return self.name