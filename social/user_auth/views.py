from rest_framework.decorators import api_view
from rest_framework.response import Response
from allauth.socialaccount.models import SocialAccount


@api_view(['GET'])
def get_user_information_from_request(request):
    if request.user.is_authenticated:
        currUser = request.user
        socialaccount = SocialAccount.objects.filter(user = currUser)
        if socialaccount.exists():
            socialaccount_instance = socialaccount[0]
            extraData = socialaccount_instance.extra_data
            user_data = socialaccount_instance.get_provider().extract_common_fields(extraData)
            user_data["picture"] = currUser.profilePhoto.url
            return Response(user_data) 
        user_data = {
            "first_name" : currUser.username,
            "picture" : currUser.profilePhoto.url
        }
        return Response(user_data)
    return Response({'msg':'unauthenticated user'})

