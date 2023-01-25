from rest_framework.routers import DefaultRouter, SimpleRouter
from discounts.views import DiscountViewSet
from gift_cards.views import GiftCardViewSet
from articles.views import ArticleViewSet
from authentication.views import UserViewSet
from partners.views import PartnerViewSet
from products.views import ProductsViewSet

router = DefaultRouter()
simrouter = SimpleRouter()

router.register('discounts', DiscountViewSet)
router.register('gift_cards', GiftCardViewSet)
router.register('articles', ArticleViewSet)
router.register('users', UserViewSet)
router.register('products', ProductsViewSet)
router.register('partners', PartnerViewSet)
