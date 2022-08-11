from rest_framework import generics, mixins
from rest_framework.permissions import IsAuthenticated

from model.models import Products
from model.serializers import ProductSerializer


class ProductListGen(generics.ListCreateAPIView):
    queryset = Products.objects.all()
    serializer_class = ProductSerializer

    
class ProductDetailGen(generics.RetrieveUpdateDestroyAPIView):
    queryset = Products.objects.all()
    serializer_class = ProductSerializer
    # permission_classes = (IsAuthenticated)