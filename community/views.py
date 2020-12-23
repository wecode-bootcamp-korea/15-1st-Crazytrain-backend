import json

from django.http import JsonResponse
from django.views import View


from .models import HouseSize, HouseStyle, HousingType, Space, Post, PostBlock
from user.utils import login_decorator
from user.models import *

class Posting(View):

    @login_decorator
    def post(self, request):
        data = json.loads(request.body)

        user         = request.user
        user_id      = user.id
        house_size   = data.get('house_size')
        house_style  = data.get('house_style')
        housing_type = data.get('housing_type')
        block        = data['block']

        try:
            post = Post.objects.create(
                user_id=user_id,
                house_size_id=house_size,
                house_style_id=house_style,
                housing_type_id=housing_type
            )

            post_block = [
                PostBlock(
                    image=item["image"],
                    content=item["content"],
                    space_id=item["space"],
                    post_id=post.id,
                ) for item in block
            ]
            PostBlock.objects.bulk_create(post_block)

            return JsonResponse({'message': "SUCCESS"}, status=201)

        except KeyError:
            return JsonResponse({"message"}, status=401)

        except TypeError:
            return JsonResponse({"message"}, status=402)

class PostDetail(View):

    def get(self, request, post_id):

        try:
            post = Post.objects.get(id=post_id)

            if post.house_size_id:
                house_size = post.house_size.size
            else:
                house_size = None

            if post.house_style_id:
                house_style = post.house_style.style
            else:
                house_style = None

            if post.housing_type_id:
                housing_type = post.housing_type.type
            else:
                housing_type = None

            result = {
                        'post' : [
                            {
                                'post_id': post.id
                            },
                            {
                                'created_at': post.created_at
                            },
                            {
                                'updated_at': post.updated_at
                            }
                        ],

                        'user' : [
                            {
                                'user_id'       : post.user.id
                            },
                            {
                                'nickname'      : post.user.nickname
                            },
                            {
                                'profile_image' : post.user.profile_image
                            }
                        ],

                        'categories' : [
                            {
                                'house_size'      : house_size
                            },
                            {
                                'house_style'     : house_style
                            },
                            {
                                'housing_type'    : housing_type
                            }
                        ],

                        'blocks' : [
                            {
                                'block_id' : block.id,
                                'post_id'  : block.post_id,
                                'image'    : block.image,
                                'content'  : block.content,
                            }
                            for block in PostBlock.objects.filter(post_id= post_id)
                        ],
                    }
            return JsonResponse({'community_detail' : result}, status=200)

        except TypeError:
            return JsonResponse({'message': "TYPE_ERROR"}, status=402)

class PostList(View):
    def get(self, request):
        try:
            order     = request.GET.get('order','')
            residence = request.GET.get('residence','')
            size      = request.GET.get('size','')
            style     = request.GET.get('style','')

            posts = Post.objects.prefetch_related(
                 'postblock_set'
            ).order_by('-id')

            if order == "1":
                posts = posts.order_by('-id')

            if order == "2":
                posts = posts.order_by('id')

            if residence:
                posts = posts.filter(housing_type_id=residence)

            if size:
                posts = posts.filter(house_size_id=size)

            if style:
                posts = posts.filter(house_style_id=style)

            results = [
                    {
                        'post_id'         : post.id,
                        'post_user_id'    : post.user.id,
                        'writer_nickname' : post.user.nickname,
                        'created_at'      : post.created_at,
                        'house_size'      : post.house_size_id,
                        'house_style'     : post.house_style_id,
                        'residence'       : post.housing_type_id,

                        'block'           : [
                        {
                            'block_image'   : block.image,
                            'block_content' : block.content
                        }
                        for block in post.postblock_set.all()
                    ],
                }
                for post in posts
            ]
            return JsonResponse({'result': results}, status=200)

        except TypeError:
            return JsonResponse({'message': 'TYPE_ERROR'}, status=402)