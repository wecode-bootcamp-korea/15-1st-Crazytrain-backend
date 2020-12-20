from django.shortcuts import render

import json

from django.http import JsonResponse
from django.views import View

from product.models import Product
from .models import HouseSize, HouseStyle, HousingType, Space,  Post, PostBlock
from user.utils import login_decorator

class Posting(View):
    @login_decorator
    def post(self, request):
        print("hi")
        data = json.loads(request.body)
        #user = data.get('user')
        house_size   = data.get('house_size')
        house_style  = data.get('house_type')
        housing_type = data.get('housing_type')
        space        = data.get('space')
        #product      = data.get('product')
        #hashtags     = data.get('hashtag')
        #product      = data.get('product')

        #user         = requset.user
        #post
        #  product ,
            # post_id 들 연결해주


        try:
            #user = request.user

            #Post.objects.create(user_id = user)

            #if product:
            #    product = Product.objects.get(name=product)
            #    Post.objects.create(product_id=product.id)

            if house_size:
                size = HouseSize.objects.get(size=house_size)
                Post.objects.create(house_size_id=size.id)

            if house_style:
                style = HouseStyle.objects.get(style=house_style)
                Post.objects.create(house_style_id=style.id)

            if housing_type:
                type = HousingType.objects.get(type=housing_type)
                Post.objects.create(housing_type_id=type.id)

            for image in data['block']:
                PostBlock.objects.create(image = image["image"])

            for content in data['block']:
                PostBlock.objects.create(content = content["content"])

            if space:
                space = Space.objects.get(space=space)
                PostBlock.objects.create(space_id = space.id)

            #post_user = Post.objects.get(user_id =user)
            #PostBlock.objects.create(post_id = post_user)

            #if hashtags:
            #    for hashtag in hashtags:
            #        Hashtag.objects.create(hashtag = hashtag)



            # 글쓰기에서 올리기를 누르면 백엔드가 데이터 없는 걸 확인하고 넘겨줘야하나.. ?
            return JsonResponse({"message":"SUCCESS"}, status=200)

        except KeyError:
            return JsonResponse({"message"}, status=401)

        except TypeError:
            return JsonResponse({"message"}, status=402)


#class PostDetailView(View):
    # 제품 추가 post
#    def post(self):


    # 수정하기
#    def put

    # 삭제하기

