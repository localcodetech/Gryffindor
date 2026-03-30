from django.shortcuts import render
from rest_framework.decorators import api_view
from .models import Product
from .serializers import ProductSerializers
from rest_framework.response import Response

# Create your views here.

@api_view(http_method_names=["GET"])
def get_product():
    product = Product.objects.all()
    serializers = ProductSerializers(product, many=True)
    return Response(serializers.data)