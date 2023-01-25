from .models import Discount
from .serializers import DiscountSerializer
from rest_framework.viewsets import ModelViewSet
from rest_framework.filters import SearchFilter
from django_filters.rest_framework import DjangoFilterBackend

class DiscountViewSet(ModelViewSet):
    queryset = Discount.objects.all()
    serializer_class = DiscountSerializer
    filter_backends = (DjangoFilterBackend, SearchFilter)
    search_fields = ('id', 'title', 'description', 'partner_name')
