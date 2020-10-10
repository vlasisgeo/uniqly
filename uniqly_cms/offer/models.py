from django.db import models

class Group(models.Model):
    name = models.CharField(max_length=250, null=True, blank=True)  

class Group_product(models.Model):
    group  = models.ForeignKey(Group, on_delete=models.CASCADE) 
    product_variant  = models.ForeignKey(Product_variant, on_delete=models.CASCADE) 

RULE_SUBJECT_CHOICES = [
    ('BASKET_SUM_PRICE', 'BASKET_SUM_PRICE'),  
    ('BASKET_COUNT', 'BASKET_COUNT'),  
    ('GROUP_PROD_SUM_PRICE', 'GROUP_PROD_SUM_PRICE'), 
    ('GROUP_PROD_COUNT', 'GROUP_PROD_SUM_NUM'),  
]

RULE_COMPARE_CHOICES = [
    ('>', 'GREATER'),  
    ('<', 'LESS'),  
    ('=', 'EQUAL'),    
]

class Offer_rules(models.Model):
    offer  = models.ForeignKey(Offer, on_delete=models.CASCADE) 
    name = models.CharField(max_length=250, null=True, blank=True)  
    rule_subject = models.CharField(max_length=20, choices = RULE_SUBJECT_CHOICES, null=True, blank=True)   
    rule_compare = models.CharField(max_length=20, choices = RULE_COMPARE_CHOICES, , null=True, blank=True)  
    rule_value = models.DecimalField(max_digits=7, decimal_places=2,null=True, blank=True)  


GIVE_TYPE_CHOICES = [
    ('GIFT', 'Gift'),    
    ('DISCOUNT_PERCENT_ALL_GROUP', 'DISCOUNT_PERCENT_ALL_GROUP'),  
    ('DISCOUNT_PERCENT_SECOND', 'DISCOUNT_PERCENT_SECOND'),  
]

class Offer_give(models.Model):
    offer  = models.ForeignKey(Offer, on_delete=models.CASCADE) 
    give_type = models.CharField(max_length=20, choices = GIVE_TYPE_CHOICES, null=True, blank=True)   
    give_value = models.DecimalField(max_digits=7, decimal_places=2,null=True, blank=True)  
    gift = models.ForeignKey(Product_variant, on_delete=models.CASCADE) 

class Offer(models.Model):
    name = models.CharField(max_length=250, null=True, blank=True)  
    route= models.ForeignKey(Route, on_delete=models.CASCADE) 
    group = models.ForeignKey(Group, on_delete=models.CASCADE) 
    active_from = models.DateTimeField(null=True, blank=True)  
    active_to = models.DateTimeField(null=True, blank=True)  
    active = models.BooleanField(default=False)  
    discount = models.DecimalField(default = 0, max_digits=4, decimal_places=2)
