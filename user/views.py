import json, bcrypt, re, jwt

from django.views import View
from django.http import JsonResponse

from .models import User
from product.models import Product
from .utils import login_decorator
from my_settings import SECRET, ALGORITHM

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


class Signup(View):
    def post(self, request):
        data           = json.loads(request.body)
        REGEX_EMAIL    = '^[a-zA-Z0-9+-_.]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
        REGEX_PASSWORD = '^[A-Za-z0-9@#$%^&+=]{8,}$'

        try:
            if not re.match(REGEX_EMAIL,data['email']):
                return JsonResponse({"message":"INVALID_MAIL"},status=401)

            if not re.match(REGEX_PASSWORD,data['password']):
                return JsonResponse({"message":"INVALID_PW"},status=401)

            if len(data['nickname']) < 2 and len(data['nickname']) > 8:
                return JsonResponse({"message":"INVALID_NICKNAME"},status=401)

            if User.objects.filter(email=data['email']).exists():
                return JsonResponse({"message":"USER_EXIST"}, status=409)

            if User.objects.filter(nickname=data['nickname']).exists():
                return JsonResponse({"message":"NICKNAME_EXIST"},status=409)

            else:
                User.objects.create(
                    email    = data['email'],
                    password = bcrypt.hashpw(data['password'].encode('utf-8'), bcrypt.gensalt()).decode(),
                    nickname = data['nickname']
                )
                return JsonResponse({"message":"SUCCESS"},status=201)

        except KeyError:
            return JsonResponse({"message":"KEY_ERROR"},status=401)
