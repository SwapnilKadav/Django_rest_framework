# In-build packages
import os

# Site packages
from django.http import JsonResponse
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view 

# applications import
from model.models import Products
from model.serializers import ProductSerializer


def ProductView(request):
    product= {
        'id': 1,
        'product_name':'Smart Watch',
        'prodcut_description':'Noise ColorFit Pulse Grand Smart Watch with 1.69"(4.29cm) HD Display, 60 Sports Modes, 150 Watch Faces, Fast Charge, Spo2, Stress, Sleep, Heart Rate Monitoring & IP68 Waterproof (Jet Black)',
        'product_price':1499,
        'product_image':'https://images-eu.ssl-images-amazon.com/images/I/41AIJsdZk-L._SX300_SY300_QL70_FMwebp_.jpg',
    }
    return JsonResponse(product)

@api_view(['GET','POST'])
def Product_list(request):
    
    if request.method =='GET':
        products = Products.objects.all()
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data)
    
    elif request.method == 'POST':
        serializer = ProductSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response (serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET','PUT','DELETE'])
def Product_detail(request,pk):
    try:
        products = Products.objects.get(pk=pk)
    except Products.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = ProductSerializer(products)
        print(type(serializer))
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = ProductSerializer(products, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        products.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)