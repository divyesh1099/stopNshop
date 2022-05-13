from django.contrib import admin
from django.contrib.admin.options import TabularInline
from .models import *
# from tinymce.widgets import TinyMCE
# Register your models here.
# admin.site.register(Product)

class ProductImageTabularInline(admin.TabularInline):
   model = ProductImage
   extra = 1

class ProductImageAdmin(admin.ModelAdmin):
   model = ProductImage
   list_display = ["product"]

class VariationStackedInline(admin.StackedInline):
   model = Variation
   readonly_fields = ["generated_variation_id"]
   extra = 0
   min_num = 1


class VariationAdmin(admin.ModelAdmin):
   model = Variation
   list_display = ["product", "name", "stock", "price"]
   search_fields = ["product__name", "name", "price"]

class ProductAdmin(admin.ModelAdmin):
   model = Product
   inlines = [ProductImageTabularInline, VariationStackedInline]
   readonly_fields = ["stock"]
   list_display = ["name", "type", "stock"]
   class Media:
      js = ("assets/js/tinyInject.js",)

admin.site.register(Material)
admin.site.register(ProductImage)
admin.site.register(Shipping)
admin.site.register(Variation, VariationAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(Type)
admin.site.register(Size)
admin.site.register(Color)