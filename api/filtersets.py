import django_filters
from api.models import Discovery, Category
from api.serializers import 
from rest_framework import generics

class ProductFilter(django_filters.FilterSet):
    min_price = django_filters.NumberFilter(name="price", lookup_type='gte')
    max_price = django_filters.NumberFilter(name="price", lookup_type='lte')
    class Meta:
        model = Product
        fields = ['category', 'in_stock', 'min_price', 'max_price']

class ProductList(generics.ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    filter_class = ProductFilter