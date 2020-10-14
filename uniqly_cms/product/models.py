from django.db import models
from django.contrib.auth.models import User
from django.utils.text import slugify


class Brand(models.Model):
    name = models.CharField(max_length=250, null=True)  
    slug = models.SlugField(unique=True, default='')

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Brand, self).save(*args, **kwargs)

class Product(models.Model):
    code = models.CharField(max_length=20, null=True)  
    name = models.CharField(max_length=250, null=True)
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
    slug = models.SlugField(unique=True, default='')

    def _generate_unique_slug(self):
        unique_slug = slugify(self.name)
        num = 1
        while Product.objects.filter(slug=unique_slug).exists():
            unique_slug = '{}-{}'.format(unique_slug, num)
            num += 1
        return unique_slug

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = self._generate_unique_slug()
        super().save(*args, **kwargs)


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
    attribute_group = models.ForeignKey(Attribute_group, on_delete=models.CASCADE, related_name='attribute_group_values')
    display_value = models.CharField(max_length=20, null=True)   
    active = models.BooleanField(default=True)  



class Product_variant(models.Model):    
    product = models.ForeignKey(Product, on_delete=models.CASCADE, blank=True, null=True, related_name='product_variants')
    variant_code =models.CharField(max_length=30, null=True)
    barcode = models.CharField(max_length=30, null=True)
    factory_code = models.CharField(max_length=20, null=True)  
    weight = models.IntegerField(default=0, blank=True)

class Product_variant_attribute(models.Model):
    attribute_value = models.ForeignKey(Attribute_value, on_delete=models.CASCADE, related_name='product_variant_attributes_values')
    product_variant = models.ForeignKey(Product_variant, on_delete=models.CASCADE, related_name='product_variant_attributes')

class Category(models.Model):
    name = models.CharField(max_length=250, null=True)
    parent =  models.ForeignKey('self', on_delete=models.CASCADE, blank=True, null=True, related_name='children')
    slug = models.SlugField(unique=True, default='')
    active = models.BooleanField(default=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Category, self).save(*args, **kwargs)

class Product_Category(models.Model):
    product =  models.ForeignKey(Product, on_delete=models.CASCADE, related_name='category_products')
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

class Country(models.Model):
    code = models.CharField(max_length=3) 
    name = models.CharField(max_length=50)  

class Vat(models.Model):
    country = models.ForeignKey(Country, on_delete=models.CASCADE) 
    code = models.CharField(max_length=10, null=True, blank=True)  
    vat_percent = models.DecimalField(default = 0, max_digits=4, decimal_places=2)

class Product_route(models.Model):
    product_variant = models.ForeignKey(Product_variant, on_delete=models.CASCADE) 
    route = models.ForeignKey(Route, on_delete=models.CASCADE) 
    price = models.DecimalField(default = 0, max_digits=7, decimal_places=2)
    discount = models.DecimalField(default = 0, max_digits=4, decimal_places=2)
    vat  = models.ForeignKey(Vat, on_delete=models.CASCADE) 
    active = models.BooleanField(default=False)

 



   

    

