from django.db.models.signals import post_save
from .models import Owner, Profile
from django.dispatch import receiver

@receiver(post_save, sender=Owner)
def create_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=Owner)
def save_profile(sender, instance, **kwargs):
    instance.profile.save()
