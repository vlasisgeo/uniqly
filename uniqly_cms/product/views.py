from django.shortcuts import render

from django.contrib.auth.models import User, Group
from .models import  Product, Brand, Product_variant, Product_variant_attribute, Attribute_value, Attribute_group, Category, Product_Category
from rest_framework import viewsets
from rest_framework import permissions
from .serializers import UserSerializer, GroupSerializer, ProductSerializer, BrandSerializer, Product_variantSerializer, Product_variant_attributeSerializer, Attribute_valueSerializer, Attribute_groupSerializer, CategorySerializer, Product_categorySerializer


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = [permissions.IsAuthenticated]

class Product_variantViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Product_variant.objects.all()
    serializer_class = Product_variantSerializer
    permission_classes = [permissions.IsAuthenticated]

class ProductViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [permissions.IsAuthenticated]

class Product_variant_attributeViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Product_variant_attribute.objects.all()
    serializer_class = Product_variant_attributeSerializer
    permission_classes = [permissions.IsAuthenticated]

class Attribute_valueViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset =Attribute_value.objects.all()
    serializer_class = Attribute_valueSerializer
    permission_classes = [permissions.IsAuthenticated]

class Attribute_groupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset =Attribute_group.objects.all()
    serializer_class = Attribute_groupSerializer
    permission_classes = [permissions.IsAuthenticated]   

class BrandViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Brand.objects.all()
    serializer_class = BrandSerializer
    permission_classes = [permissions.IsAuthenticated]


        


class CategoryViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [permissions.IsAuthenticated]

class Product_categoryViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Product_Category.objects.all()
    serializer_class = Product_categorySerializer
    permission_classes = [permissions.IsAuthenticated]