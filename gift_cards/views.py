from .models import GiftCard, FavouriteGiftCard
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated
from .serializers import GiftCardSerializer
from rest_framework.viewsets import ModelViewSet
from .serializers import FavouriteGiftCardSerializer
from rest_framework.response import Response
from rest_framework.filters import SearchFilter
from django_filters.rest_framework import DjangoFilterBackend
from django.db.models import Q

class GiftCardViewSet(ModelViewSet):
    queryset = GiftCard.objects.all()
    serializer_class = GiftCardSerializer
    filter_backends = (DjangoFilterBackend, SearchFilter)
    search_fields = ('id', 'name', 'description')

    @action(methods=['POST'], detail=True, permission_classes=[IsAuthenticated], url_path='add-favourite')
    def add_favourite(self, request,pk=None):
        user = request.user
        gift_card = self.queryset.get(pk=pk)
        try:
            gift_card = FavouriteGiftCard.objects.get(user=user, gift_card=gift_card)
            gift_card.delete()
            return Response({'message': 'Купон удалён из избранных'})
        except FavouriteGiftCard.DoesNotExist:
            FavouriteGiftCard.objects.create(user=user, gift_card=gift_card)
            return Response({'message': 'Купон добавлен в избранные'})

    @action(methods=['GET'], detail=False, permission_classes=[IsAuthenticated], url_path='favourites')
    def get_favourites(self, request):
        user = request.user
        gift_card = GiftCard.objects.filter(user=user)
        data = FavouriteGiftCardSerializer(instance=gift_card, many=True).data
        return Response(data)

    @action(methods=['GET'], detail=False, url_path='dodo')
    def get_dodo(self, gift_cards):
        gift_cards = GiftCard.objects.filter( Q(partner_name__exact=1))
        data = GiftCardSerializer(instance=gift_cards, many=True).data
        return Response(data)
