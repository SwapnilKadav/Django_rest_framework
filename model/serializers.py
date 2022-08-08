from rest_framework import serializers
from model.models import Products

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model= Products
        fields = ['id','product_name','prodcut_description','product_price','product_image']
