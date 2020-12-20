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
#[img.url for img in product.productimage_set.all()]
class ProductListView(View):
     def get(self, request):
        try:                            #역참조
            products = Product.objects.prefetch_related('productimage_set','option_set').select_related('sub_category','package','brand','sale').all()
           
            if products.exists():
                 products = [{ 
                  'alt' : product.name,
                  '이미지url': image.url,
                  '제목': product.package.name,
                  '가격': int(str(option.price).split(".")[0]), # 소수점 제거
                  '브랜드': product.brand.name,
                  'itemBadge': product.sale.name
            } for product in products
             for image in product.productimage_set.all()
             for option in product.option_set.all()]
            
            
               
        #    categories = Category.objects.prefetch_related('subcategory_set').all()
        #    if categories.exists():   
        #        categories = [{ 
        #         'categoryId'   : category.id,
        #         'category'     : category.name,
        #         'subCategories': [
        #             sub_category.name
        #        for sub_category in category.subcategory_set.all()]
        #    } for category in categories]

            return JsonResponse({"test": products}, status=200)

        except ValueError:
            return JsonResponse({'message':'VALUE_ERROR'}, status=400)
        # except:
        #     return JsonResponse({'message':'제발 되게 해줘'}, status=400)
            