from django.db.models.signals import post_save
from django.dispatch import receiver
from allauth.socialaccount.models import SocialAccount
from allauth.socialaccount.signals import pre_social_login
import urllib
from django.core.files import File



@receiver(post_save, sender=SocialAccount)
def my_handler(sender,instance,created, **kwargs):
    if created:
        profile_photo_url = SocialAccount.objects.filter(user = instance.user)[0].get_avatar_url()
        response = urllib.request.urlopen(profile_photo_url)
        instance.user.profilePhoto.save(
            f'{instance.user.username}{instance.provider}.png',
            File(response),
            save=True
            )
        
@receiver(pre_social_login)        
def socialAccountLogin(request,sociallogin,**kwargs):
    print(f'{sociallogin.user} logged in')