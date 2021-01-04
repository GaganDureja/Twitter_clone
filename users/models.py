from django.db import models
from django.contrib.auth.models import User

# Create your models here.



class Profile(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE)	
	mobile = models.CharField(max_length=12, blank=True)
	
	

	# def __str__(self):
	# 	return self.user.username


# def create_user_profile(sender, instance, created, **kwargs):
# 	if created:
# 		Profile.objects.create(user=instance)


#post_save.connect(create_user_profile, sender=User)