import jwt
from django.http import JsonResponse
from my_settings import SECRET, ALGORITHM
from user.models import User

def login_decorator(func):
    def wrapper(self, request, *args, **kwargs):
        if "Authorization" is None:
            return JsonResponse({"MESSAGE":"INVALID_LOGIN"}, status=401)
        encode_token = request.header["Authorization"]
        try:
            data         = jwt.decode(encode_token, SECRET, ALGORITHM)
            user         = User.objects.get(id = data["id"])
            request.user = user        
        except jwt.DecodeError:
            return JsonResponse({"MESSAGE" : "INVALID_TOKEN"}, status = 401)
        except User.DoesNotExist:
            return JsonResponse({"MESSAGE" : "INVALID_USER"}, status = 401) 
        except jwt.InvalidTokenError:
            return JsonResponse({'MESSAGE': 'INVALID_ACCESS_TOKEN'}, status=401)       
        return func(self, request, *args, **kwargs)
    return wrapper