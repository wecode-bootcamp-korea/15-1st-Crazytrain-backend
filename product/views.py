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
#[image.url for image in product.productimage_set.all()],
        context = [{
            'id'           : product.package.id,
            'alt'          : product.package.name,
            'product_image': [image.url for image in product.productimage_set.all()],
            'articleName'  : product.package.name,
            'brandName'    : product.brand.name,
            'ispackage'    : "true",
            'itemBadge'    : product.sale.name,
            'options'      : [{'color':option.option_color.name,'price':int(option.price)
                            } for option in product.option_set.all()]
        }for product in products]
        return JsonResponse({"productlist": context}, status=200)
class ProductDetailView(View):
     def get(self, request, package_id):
        try:
            Image.objects.filter(product=product.id)
            products = Product.objects.prefetch_related(
            'productimage_set',
            'option_set').select_related(
            'sub_category').filter(
            package_id=package_id)
            context = [{
                'id'           : product.id,
                'productName'  : product.name,
                'product_image': [image.url for image in product.productimage_set.all()],
                'brandName'    : product.brand.name,
                'articleName'  : product.package.name,
                'alt'          : product.package.name,
                'sub_category' : product.sub_category.name,
                'options'      : [{'color':option.option_color.name,'price':int(option.price)
                                 } for option in product.option_set.all()],
                'ispackage'    : "true",
                'itemBadge'    : product.sale.name,
                'infoImage'    : product.information_image,
                'category'     : Category.objects.get(id=1).name
            }for product in products]
            return JsonResponse({'productdetail' :context}, status=200)
        except Product.DoesNotExist:
             return JsonResponse({'MESSAGE':'NO_PRODUCT'}, status=404)
        except ValueError:
            return JsonResponse({'message':'VALUE_ERROR'}, status=400)