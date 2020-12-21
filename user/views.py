import json, bcrypt, re
from django.views import View
from django.http import JsonResponse
from .models import User,History
from product.models import Product


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