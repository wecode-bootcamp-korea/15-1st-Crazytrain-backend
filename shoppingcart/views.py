import json, re, bcrypt, jwt

from django.views import View
from django.http import JsonResponse

from .models import Cart
from user.models import User
from product.models import Product, OptionSize, OptionColor, Option
from user.utils  import login_decorator
from my_settings import SECRET, ALGORITHM

class Cart(View):
    #장바구니 등록
    @login_decorator
    def post(self, request):
        try:
            data = json.loads(request.body)
            #필터값이 맞으면(흠.. size랑 color가 어려운데..)
            user = request.user
            
            if Cart.objects.filter(user=request.user.id, product=data['product_id'], size=data['size_id'],color=data['color_id']):
                item = Cart.objects.get(user=user.id, product=data['product_id'], size=data['size_id'],color=data['color_id'])
                #뭔값이 나올라나...?
                print(item)
                item.quantity += data['quantity']
                item.save()
            
            else: #아니면?.. 흠
                #추가
                Cart.objects.create(
                    user     = User(id = user.id),
                    product  = Product(id = data['product_id']),
                    quantity = data['quantity'],
                    size     = OptionSize(id = data['size_id']),
                    color    = OptionColor(id = data['color_id'])
                )
            return JsonResponse({"message":"SUCCESS"}, status=201)
       
        except KeyError as ex:
            return JsonResponse({"message":"KEY_ERROR_" + ex.args[0]}, status=400)
        except Exception as ex:
            return JsonResponse({"message":"ERROR_" + ex.args[0]}, status=400)


        