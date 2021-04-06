from  django.db.models.signals import post_save# this is a signal that gets 
from django.contrib.auth.models import User#sender of signal
from django.dispatch import receiver
from .models import Profile
#reciever will be a function that recives this signal and performs a task

@receiver(post_save,sender=User)
def create_profile(sender,instance,created,**kwargs	):
	if created:
		Profile.objects.create(user=instance)

@receiver(post_save,sender=User)
def save_profile(sender,instance,**kwargs):
	
	instance.profile.save()