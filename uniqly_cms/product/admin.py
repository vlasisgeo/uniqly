from django.contrib import admin

from .models import Product, Product_variant, Brand, Product_variant_attribute, Attribute_value, Attribute_group, Category, Product_Category

class BrandAdmin(admin.ModelAdmin):
    list_display = ('name',)

class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'code', 'brand','created_at')
   
class Product_variantAdmin(admin.ModelAdmin):
    list_display = ('product', 'variant_code','barcode')

class Product_variant_attributeAdmin(admin.ModelAdmin):
    list_display = ('attribute_value', 'product_variant')

class Attribute_valueAdmin(admin.ModelAdmin):
    list_display = ('attribute_group', 'display_value', 'active')

class Attribute_groupAdmin(admin.ModelAdmin):
    list_display = ('name', 'display_type', 'active')

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'parent', 'active')

class Product_CategoryAdmin(admin.ModelAdmin):
    list_display = ('product', 'category')

admin.site.register(Product, ProductAdmin)
admin.site.register(Product_variant, Product_variantAdmin)
admin.site.register(Product_variant_attribute, Product_variant_attributeAdmin)
admin.site.register(Attribute_group, Attribute_groupAdmin)
admin.site.register(Attribute_value, Attribute_valueAdmin)
admin.site.register(Brand, BrandAdmin)
admin.site.register(Product_Category, Product_CategoryAdmin)
admin.site.register(Category, CategoryAdmin)
