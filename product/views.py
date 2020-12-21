import json

from django.views import View
from django.http import JsonResponse

from menu.models import Category, SubCategory
from .models import (
    Package,
    Product,
    OptionSize,
    OptionColor,
    Option,
    ProductImage
)


class ProductView(View):
     def get(self, request):
        # 가격순 추가 구현
        products = Product.objects.prefetch_related(
            'productimage_set',
            'option_set').select_related(
            'sub_category',
            'package',
            'brand',
            'sale'
            ).all()
        
        if products.exists():

            products = [{ 
            'alt' : product.name,
            '이미지url': image.url,
            '제목': product.package.name,
            '가격': int(str(option.price).split(".")[0]),
            '브랜드': product.brand.name,
            'itemBadge': product.sale.name
             # 리뷰 개수 추가 구현
            # 리뷰 평점 추가 구현
            } for product in products
            for image in product.productimage_set.all()
            for option in product.option_set.all()]
        
            return JsonResponse({"test": products}, status=200)

        
    
class ProductDetailView(View):
    def get(self, request, product_id):
        try:
            product = Product.objects.prefetch_related(
                'productimage_set',
                'option_set').select_related(
                'sub_category',
                'package',
                'brand',
                'sale'
                ).get(id=product_id)
            
            test = [{
                '제목': product.package.name,
                '브랜드': product.brand.name,
                #'대표가격': int(str(option.price).split(".")[0]),
                '추가정보':[
                    product.name
                ]
            }for option in product.option_set.all()]
            
            categories = Category.objects.prefetch_related('subcategory_set').all()

        # categories = [{ 
        #     'categoryId'   : category.id,
        #     'category'     : category.name,
        #     'subCategories': [
        #         sub_category.name
        #         for sub_category in category.subcategory_set.all()]
        #     } for category in categories]
            return JsonResponse({'제발..' :test}, status=200)

        except Product.DoesNotExist:
            return JsonResponse({'MESSAGE' : 'NO_PRODUCT'}, status=404)


