from ..settings import SESSION_COOKIE_SAMESITE

class CustomSameSiteMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        print(f'User -> {request.user}')
        response = self.get_response(request)
        


        return response