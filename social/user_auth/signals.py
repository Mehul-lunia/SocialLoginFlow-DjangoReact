from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import CustomUserModel
from allauth.socialaccount.models import SocialAccount
import urllib
from django.core.files import File
from PIL import Image


@receiver(post_save, sender=SocialAccount)
def my_handler(sender,instance,created, **kwargs):
    if created:
        extrData = SocialAccount.objects.filter(user = instance.user)[0].extra_data
        if instance.provider == 'google':
            profile_photo_url = extrData.get('picture')
        elif instance.provider == 'github':
            profile_photo_url = extrData.get('avatar_url')
        response = urllib.request.urlopen(profile_photo_url)
        instance.user.profilePhoto.save(
            f'{instance.user.username}{instance.provider}.png',
            File(response),
            save=True
            )
        
        
        print(f'Binary Image -> {response}')