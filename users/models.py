from django.db import models
from django.contrib.auth.models import User

# Create your models here.



class Profile(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE)
	mail = models.EmailField(max_length=254)
	mobile = models.IntegerField()
	dob = models.DateField()

	def __str__(self):
		return self.user