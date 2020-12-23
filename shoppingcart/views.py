import json, re, bcrypt, jwt

from django.views import View
from django.http import JsonResponse

from .models import Cart
from user.models import User
from product.models import Product, OptionSize, OptionColor, Option
from user.utils  import login_decorator
from my_settings import SECRET, ALGORITHM

class CartView(View):
    #장바구니 등록
    @login_decorator
    def post(self, request):
        data = json.loads(request.body)
        user = request.user
        try:   
            if Cart.objects.filter(
                user=user.id, 
                product=data['product_id'], 
                size=data['size_id'],
                color=data['color_id']).exists():
                item = Cart.objects.get(
                    user=user.id, 
                    product=data['product_id'], 
                    size=data['size_id'],
                    color=data['color_id'],
                    price=data['price_id'])
                item.quantity += int(data['quantity'])
                item.save()
                    
            Cart.objects.create(
                user     = User(id = user.id),
                product  = Product(id = data['product_id']),
                quantity = int(data['quantity']),
                size     = OptionSize(id = data['size_id']),
                color    = OptionColor(id = data['color_id']),
                price    = Option(id = data['price_id'])
            )
            return JsonResponse({"message":"SUCCESS"}, status=201)
        
        except KeyError as ex:
            print(data)
            return JsonResponse({"message":"KEY_ERROR_" + str(ex.args[0])}, status=400)

    #장바구니 조회
    @login_decorator
    def get(self, request):
        user = request.user
        try:
            cart_list = [{
                'id'          : item.id,
                'user_id'     : item.user_id,
                'product_id'  : item.product_id,
                'product_name': item.product.name,
                'quantity'    : item.quantity,
                'size'        : item.size.name,
                'color'       : item.color.name,
                'price'       : item.price.price,
                'image_url'   : item.product.information_image
            } for item in Cart.objects.filter(user=user.id)]
            return JsonResponse({'message':'SUCCESS', 'CART_LIST': cart_list}, status=200)
        
        except KeyError:
            return JsonResponse({'message':'KEY_ERROR'}, status=400)
