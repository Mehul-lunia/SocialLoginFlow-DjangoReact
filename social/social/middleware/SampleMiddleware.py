from ..settings import SESSION_COOKIE_SECURE
import os

class CustomSameSiteMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        # print(f'User -> {os.getenv("USE_SECURE_COOKIES")}')
        response = self.get_response(request)
        


        return response