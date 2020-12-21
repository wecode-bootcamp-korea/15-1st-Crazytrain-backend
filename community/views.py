from django.shortcuts import render

import json

from django.http import JsonResponse
from django.views import View

from product.models import Product
from .models import HouseSize, HouseStyle, HousingType, Space,  Post, PostBlock
#from user.utils import login_decorator
from product.models import *

class Posting(View):

    #@login_decorator
    def post(self, request):
        data = json.loads(request.body)

        # 토큰 전까지 사용할  유저 아이디
        user_id = 2

        house_size   = data.get('house_size')
        house_style  = data.get('house_style')
        housing_type = data.get('housing_type')
        block = data['block']

        try:
            Post.objects.create(
                user_id=user_id,
                house_size_id=house_size,
                house_style_id=house_style,
                housing_type_id=housing_type
            )

            post = Post.objects.all().last()

            for i in block:
                PostBlock.objects.create(
                    image=i["image"],
                    content=i["content"],
                    space_id = i["space"],
                    post_id=post.id,
                )

        except KeyError:
            return JsonResponse({"message"}, status=401)
        #
        except TypeError:
            return JsonResponse({"message"}, status=402)


#class PostDetailView(View):
    # 제품 추가 post
#    def post(self):


    # 수정하기
#    def put

    # 삭제하기
