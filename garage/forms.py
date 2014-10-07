from django.forms import ModelForm
from models import Builder,Team,Part
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class BuildersForm(ModelForm):
	class Meta: 
		model = Builder
		fields = ['name','year','bio']

class TeamForm(ModelForm):
	class Meta:
		model = Team
		fields = ['name','description']

class PartForm(ModelForm):
	class Meta:
		model = Part
		fields = ['name','source', 'count','cost']

class UserForm(UserCreationForm):
	class Meta:
		model = User
		fields = ["username","email"]