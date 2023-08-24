from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response


@api_view(['GET'])
def home(request):
    currUser = request.user.username
    response = Response({'msg':currUser})
    return response