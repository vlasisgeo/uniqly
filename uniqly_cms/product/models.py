from django.db import models
from django.contrib.auth.models import User

OFFER_TYPE_CHOICES = [
    ('GIFT', 'Gift'),
    
]



DISPLAY_TYPE_CHOICES = [
    ('TEXT', 'Text'),
    ('HEX', 'HEX Color'),  
    ('IMG', 'Image'), 
]
class Attribute_group(models.Model):
    name = models.CharField(max_length=20, null=True)   
    display_type = models.CharField(max_length=20, default='TEXT', choices = DISPLAY_TYPE_CHOICES)   
    active = models.BooleanField(default=True)  

class Attribute_value(models.Model):
    attribute_group = models.ForeignKey(Attribute_group, on_delete=models.CASCADE)
    display_value = models.CharField(max_length=20, null=True)   
    active = models.BooleanField(default=True)  

class Product_variant_attribute(models.Model):
    attribute_value = models.ForeignKey(Attribute_value, on_delete=models.CASCADE)
    product_variant = models.ForeignKey(Product_variant, on_delete=models.CASCADE)

class Product_variant(models.Model):    
    product = models.ForeignKey(Product, on_delete=models.CASCADE, blank=True, null=True)
    variant_code =models.CharField(max_length=30, null=True)
    barcode = models.CharField(max_length=30, null=True)
    factory_code = models.CharField(max_length=20, null=True)  
    weight = models.IntegerField(default=0, blank=True)


class Product(models.Model):
    code = models.CharField(max_length=20, null=True)  
    name = models.CharField(max_length=250, null=True)
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)


class Brand(models.Model):
    name = models.CharField(max_length=250, null=True)  

class Category(models.Model):
    name = models.CharField(max_length=250, null=True)  
    parent =  models.ForeignKey(Category, on_delete=models.CASCADE, blank=True, null=True)


class Product_Category(models.Model):
    product =  models.ForeignKey(Product, on_delete=models.CASCADE)
    category =  models.ForeignKey(Category, on_delete=models.CASCADE)


class Warehouse(models.Model):
    code = models.CharField(max_length=20, null=True)       
    name = models.CharField(max_length=50, null=True)  

class Stock(models.Model):
    product_variant = models.ForeignKey(Product_variant, on_delete=models.CASCADE)
    warehouse = models.ForeignKey(Warehouse, on_delete=models.CASCADE)
    qty =  models.IntegerField(default=0, blank=True)
    

class Zone(models.Model):   
    name = models.CharField(max_length=250, null=True, blank=True)  
    description = models.TextField(null=True, blank=True)  


class Route(models.Model):       
    name = models.CharField(max_length=250, null=True, blank=True)  
    description = models.TextField(max_length=250, null=True, blank=True) 
    zone = models.ForeignKey(Zone, on_delete=models.CASCADE) 
    warehouse = models.ForeignKey(Warehouse, on_delete=models.CASCADE) 


class Product_route(models.Model):
    product_variant = models.ForeignKey(Product_variant, on_delete=models.CASCADE) 
    route = models.ForeignKey(Route, on_delete=models.CASCADE) 
    price = models.DecimalField(default = 0, max_digits=7, decimal_places=2)
    discount = models.DecimalField(default = 0, max_digits=4, decimal_places=2)
    vat  = models.ForeignKey(Vat, on_delete=models.CASCADE) 
    active = models.BooleanField(default=False)



    
class Country(models.Model):
    code = models.CharField(max_length=3) 
    name = models.CharField(max_length=50)  

class Vat(models.Model):
    country = models.ForeignKey(Country, on_delete=models.CASCADE) 
    code = models.CharField(max_length=10, null=True, blank=True)  
    vat_percent = models.DecimalField(default = 0, max_digits=4, decimal_places=2)


   

    

