from django.contrib.auth.models import User, Group
from .models import Product, Brand, Product_variant, Product_variant_attribute, Attribute_value, Attribute_group
from rest_framework import serializers


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'groups']


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ['url', 'name']

class Attribute_groupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Attribute_group
        fields = [ 'name', 'display_type', 'active']

#Attribute_value
class Attribute_valueSerializer(serializers.ModelSerializer):     
    class Meta:
        model = Attribute_value
        fields = ['display_value',  'active']
        
#Product_variant
class Product_variant_attributeSerializer(serializers.ModelSerializer):  
    product_variant_attributes_values = Attribute_valueSerializer(read_only=True)    
    class Meta:
        model = Product_variant_attribute
        fields = ['attribute_value', 'product_variant_attributes_values']
        depth = 2

class Product_variantSerializer(serializers.ModelSerializer):     
    product_variant_attributes = Product_variant_attributeSerializer(many=True, read_only=True)
    
    class Meta:
        model = Product_variant
        fields = ['variant_code', 'barcode', 'weight',  'product_variant_attributes']


class ProductSerializer(serializers.ModelSerializer):
    product_variants = Product_variantSerializer(many=True, read_only=True)

    class Meta:
        model = Product
        fields = ['code', 'name', 'brand', 'slug', 'product_variants']

class BrandSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['name', 'slug']

