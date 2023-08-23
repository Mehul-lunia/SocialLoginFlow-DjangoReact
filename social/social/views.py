from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response

@api_view(['GET'])
def home(request):
    print(request._request.user)
    currUser = request.user.username
    return Response({'msg':currUser})