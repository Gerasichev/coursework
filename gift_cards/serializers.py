from rest_framework import serializers
from .models import GiftCard, FavouriteGiftCard
from authentication.serializers import UserSerializer

class GiftCardSerializer(serializers.ModelSerializer):
    class Meta:
        model = GiftCard
        fields = '__all__'
    def validate(self, data):
        if data['name'] == data['description']:
            raise serializers.ValidationError('Название и описание должны различаться!')
        return data

class FavouriteGiftCardSerializer(serializers.ModelSerializer):
    user_data = UserSerializer(source='user')
    gift_card_data = GiftCardSerializer(source='gift_card')

    class Meta:
        model = FavouriteGiftCard
        exclude = ['user', 'gift_card']