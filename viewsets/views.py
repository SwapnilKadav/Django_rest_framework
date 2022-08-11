from rest_framework import viewsets

from model.models import Products
from model.serializers import ProductSerializer
from rest_framework import permissions, authentication

class ProductViewSet(viewsets.ModelViewSet):
    permission_classes = [permissions.IsAuthenticated, ]
    authentication_classes= [authentication.TokenAuthentication, authentication.SessionAuthentication]
    queryset = Products.objects.all()
    serializer_class = ProductSerializer
    