import json, bcrypt, re

from django.views import View
from django.http import JsonResponse

from .models import User,History
from product.models import Product
from .utils import login_decorator


class Signin(View):
    def post(self, request):
        data = json.loads(request.body)
        try:
            if User.objects.all().filter(email=data['email']).exists():
                if bcrypt.checkpw(data['password'].encode('utf-8'),User.objects.get(email=data['email']).password.encode('utf-8')):
                    access_token = jwt.encode({'id':User.objects.get(email=data['email']).id}, SECRET, ALGORITHM).decode('utf-8')
                   
                    return JsonResponse({"message":"SUCCESS", "TOKEN":access_token}, status=200)

                return JsonResponse({"message":"INVALID_PW"},status=401)
            return JsonResponse({"message":"INVALID_EMAIL"},status=401)
        except KeyError:
            return JsonResponse({"message":"KEY_ERROR"},status=403)
        except ValueError:
            return JsonResponse({"message":"INVALID_USER"},status=404)