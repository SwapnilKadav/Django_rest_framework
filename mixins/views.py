from rest_framework import generics, mixins
from rest_framework.permissions import IsAuthenticated

from model.models import Products
from model.serializers import ProductSerializer

class ProductListMixins(mixins.ListModelMixin, mixins.CreateModelMixin, generics.GenericAPIView):
    queryset = Products.objects.all()
    serializer_class = ProductSerializer

    def get(self, request):
        return self.list(request)
    def post(self, request):
        return self.create(request)
        
    
class ProductDetailmixins(mixins.RetrieveModelMixin, mixins.UpdateModelMixin, mixins.DestroyModelMixin, generics.GenericAPIView):
    queryset = Products.objects.all()
    serializer_class = ProductSerializer

    def get(self, request, pk):
        return self.retrive(request, pk)

    def put(self, request, pk):
        return self.update(request, pk)

    def delete(self, request , pk):
        return self.destroy(request, pk)

