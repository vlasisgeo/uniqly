"""uniqly_cms URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from product import views

from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'groups', views.GroupViewSet)
router.register(r'products', views.ProductViewSet)
router.register(r'product_variants', views.Product_variantViewSet)
router.register(r'product_variant_attributes', views.Product_variant_attributeViewSet)
router.register(r'attribute_values', views.Attribute_valueViewSet)
router.register(r'attribute_group', views.Attribute_groupViewSet)
router.register(r'brands', views.BrandViewSet)
router.register(r'brand/<str:pk>/', views.BrandViewSet)
router.register(r'categories', views.CategoryViewSet)
router.register(r'product_category', views.Product_categoryViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    path('api-auth/', include('rest_framework.urls'),  name='rest_framework'),
]
