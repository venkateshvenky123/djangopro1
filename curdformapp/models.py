from django.db import models

from django.db import models

class productdata(models.Model):
    product_id=models.IntegerField()
    product_name=models.CharField(max_length=100)
    product_class=models.CharField(max_length=100)
    product_color=models.CharField(max_length=100)
    product_cost=models.IntegerField()