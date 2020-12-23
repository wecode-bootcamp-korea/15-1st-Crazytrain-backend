import json
from django.views import View
from django.http import JsonResponse
from menu.models import Category, SubCategory
from product.models import (
    Package,
    Product,
    OptionSize,
    OptionColor,
    Option,
    ProductImage
)
class ProductListView(View):
     def get(self, request):
        sub_category_id  = request.GET.get("sub", None)
        products = Product.objects.prefetch_related(
            'productimage_set',
            'option_set').select_related(
            'sub_category').filter(
            sub_category_id=sub_category_id)
        
        context = [{
            'id'            : product.package.id,
            'alt'           : product.package.name,
            'images'        : [image.url for image in product.productimage_set.all()],
            'articleName'   : product.package.name,
            'brandName'     : product.brand.name,
            'ispackage'     : "true",
            'itemBadge'     : "",
            'options'       : [{'color':option.option_color.name,'price':int(option.price)} for option in product.option_set.all()]
        }for product in products]

        return JsonResponse({"productlist": context}, status=200)

class ProductDetailView(View):
     def get(self, request, package_id):
         try:
            packages = Package.objects.prefetch_related('product_set').get(id=package_id)
            context = [{
                '상품제목': product.package.name,
                '상품이름': product.name,
                '상품id' : product.id,
                '가격'   : int(str(option.price).split(".")[0]),
                '옵션id' : option.id,
                '옵션색깔': option.option_color.name,
                '상품사진': image.url
            } for product in packages.product_set.all() 
            for option in Option.objects.filter(product=product.id) for image in ProductImage.objects.filter(product=product.id)]
            return JsonResponse({'productdetail' :context}, status=200)
         except Product.DoesNotExist:
             return JsonResponse({'MESSAGE':'NO_PRODUCT'}, status=404)
         except ValueError:
             return JsonResponse({'message':'VALUE_ERROR'}, status=400)