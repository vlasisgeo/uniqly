from django.db import models


class Order(models.Model):    
    serial_number = models.CharField(max_length=20, null=True)  

 
    
