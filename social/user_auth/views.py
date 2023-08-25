from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from allauth.socialaccount.models import SocialAccount






@api_view(['GET'])
def get_user_information_from_request(request):
    if request.user.is_authenticated:
        currUser = request.user
        socialaccount_instance = SocialAccount.objects.filter(user = currUser)[0]
        extraData = socialaccount_instance.extra_data
        if socialaccount_instance.provider == 'github':

            user_data = {
                "provider"   : socialaccount_instance.provider,
                "username"   : extraData['login'],
                "avatar_url" : currUser.profilePhoto.url,
                "html_url"   : extraData.get('html_url'),
                "email"      : extraData.get('email'),
            }
            return Response(user_data) 
        elif socialaccount_instance.provider == 'google':
            user_data = {
                "provider":socialaccount_instance.provider,
                "name"    : extraData.get('name'),
                "picture" :currUser.profilePhoto.url,
            }
            return Response(user_data)
        return Response({'msg':request.user.username})
    return Response({'msg':'unauthenticated user'})

