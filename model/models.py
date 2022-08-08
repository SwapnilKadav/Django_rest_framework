from django.db import models

class Products(models.Model):
    product_name = models.CharField(max_length=20)
    prodcut_description = models.CharField(max_length=200)
    product_price = models.DecimalField(max_digits=10,decimal_places=2)
    product_image = models.CharField(max_length=500) 

    def __str__(self):
        return self.product_name+self.prodcut_description+self.product_price+self.product_image


