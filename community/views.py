from django.shortcuts import render
import json

from django.http import JsonResponse
from django.views import View

from .models import HouseSize, HouseStyle, HousingType, Space,  Post, PostBlock
#from user.utils import login_decorator
from product.models import *
from user.models import *

class Posting(View):

    #@login_decorator
    def post(self, request):
        data = json.loads(request.body)

        # 토큰 전까지 사용할  유저 아이디
        user_id      = 2

        house_size   = data.get('house_size')
        house_style  = data.get('house_style')
        housing_type = data.get('housing_type')
        block        = data['block']

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
            return JsonResponse({'message': "SUCCESS"}, status=200)

        except KeyError:
            return JsonResponse({"message"}, status=401)
        #
        except TypeError:
            return JsonResponse({"message"}, status=402)


class PostDetail(View):

    def get(self, request, post_id):

        try:
            post  = Post.objects.get(id=post_id)
            user  = User.objects.get(id=post.user_id)


            result = {
                        'post_id'         : post.id,
                        'created_at'      : post.created_at,
                        'updated_at'      : post.updated_at,

                        'user' : {
                            'user_id'       : user.id,
                            'nickname'      : user.nickname,
                            'profile_image' : user.profile_image
                        },

                        'categories': {
                        'house_size'      : HouseSize.objects.get(id=post.house_size_id).size,
                        'house_style'     : HouseStyle.objects.get(id=post.house_style_id).style,
                        'housing_type'    : HousingType.objects.get(id=post.housing_type_id).type
                        },

                        'blocks' : [
                            {
                                'block_id' : block.id,
                                'post_id'  : block.post_id,
                                'image'    : block.image,
                                'content'  : block.content,
                                'space'    : Space.objects.get(id=block.space_id).space
                            }
                            for block in PostBlock.objects.filter(post_id= post_id)
                        ]

            }

            return JsonResponse({'results' : result}, status = 200)


        except KeyError:
            return JsonResponse({'message': "error"}, status=401)