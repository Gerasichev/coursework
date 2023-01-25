from .models import Partner
from .serializers import PartnerSerializer
from rest_framework.viewsets import ModelViewSet
from rest_framework.filters import SearchFilter
from django_filters.rest_framework import DjangoFilterBackend

class PartnerViewSet(ModelViewSet):
    queryset = Partner.objects.all()
    serializer_class = PartnerSerializer
    filter_backends = (DjangoFilterBackend, SearchFilter)
    search_fields = ('id', 'name')
