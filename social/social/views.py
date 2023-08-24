from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from allauth.socialaccount.views import ConnectionsView


@api_view(['GET'])
def home(request):
    currUser = request.user.username
    print(request.user.socialaccount_set.all()[0].extra_data)
    response = Response({'msg':currUser})
    return response